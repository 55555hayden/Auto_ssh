# Auto_ssh 

## O script utiliza Python e a biblioteca Paramiko(http://www.paramiko.org/) que fornece uma interface SSH/SFTP para:

- Conectar a um servidor remoto via SSH
- Criar um diretório remoto (se necessário)
- Transferir um arquivo de um computador local para o servidor
- Verificar se o arquivo foi transferido com sucesso

## Funcionalidades

- Conexão SSH segura com autenticação por usuário e senha
- Execução de comandos remotos via SSH
- Criação automática do diretório remoto
- Transferência de arquivos via SFTP
- Verificação final via `ls -l` no servidor remoto

## Requisitos 

- Python 3.6+
- Biblioteca `paramiko`

## Você pode instalar a dependência com:

pip install paramiko

## Ativação

python organizador.py


## Avisos de Segurança

Não armazene sua senha em texto para produção. Use variáveis de ambiente ou arquivos seguros.
Cuidado! AutoAddPolicy() aceita qualquer chave do host automaticamente.
