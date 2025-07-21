import paramiko
import os

class SSHManager:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def connect(self, hostname):
        self.ssh.connect(hostname=hostname, 
                         username=self.username, password=self.password)
    
    def execute_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        output = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')
        exit_code = stdout.channel.recv_exit_status()
        return exit_code, output

    def copy_file_to_remote(self, localfile, remotefile):
        sftp = self.ssh.open_sftp()
        sftp.put(localfile, remotefile)
        sftp.close()

    def close(self):
        self.ssh.close()

def main():
    
    username = "seu_usuario_ssh"
    password = "sua_senha_ssh"
    hostname = "ip_do_servidor"
    
    # Arquivo a ser transferido
    arquivo_local = r"path_local"
    diretorio_remoto = "path_servidor"
    
    ssh_manager = SSHManager(username, password)
    try:
        print(f"Conectando ao servidor {hostname}...")
        ssh_manager.connect(hostname)
        
        # Verifica se o arquivo local existe
        if not os.path.exists(arquivo_local):
            print(f"ERRO: Arquivo local não encontrado: {arquivo_local}")
            return
        
        # Cria diretório remoto se necessário
        nome_arquivo = os.path.basename(arquivo_local)
        arquivo_remoto = os.path.join(diretorio_remoto, nome_arquivo).replace("\\", "/")
        
        # Comando para criar diretório remoto (se não existir)
        ssh_manager.execute_command(f"mkdir -p {diretorio_remoto}")
        
        # Transferência do arquivo
        print(f"Transferindo: {arquivo_local} -> {arquivo_remoto}")
        ssh_manager.copy_file_to_remote(arquivo_local, arquivo_remoto)
        
        # Verificação
        exit_code, output = ssh_manager.execute_command(f"ls -l {arquivo_remoto}")
        if exit_code == 0:
            print("Transferência realizada com sucesso!")
            print("Detalhes do arquivo remoto:")
            print(output)
        else:
            print("Falha na verificação do arquivo remoto")
    
    except Exception as e:
        print(f"Erro durante a operação: {str(e)}")
    finally:
        ssh_manager.close()
        print("Conexão encerrada")

if __name__ == "__main__":
    main()
