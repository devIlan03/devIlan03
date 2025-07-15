# Automatizador de envio de e-mails

Este repositório contém um script simples em Python para automatizar o envio de e-mails utilizando SMTP.

## Requisitos
- Python 3.10 ou superior.
- Um servidor SMTP (ex.: Gmail, Outlook) e as credenciais de acesso.

## Configuração
As informações do servidor e credenciais devem ser fornecidas por meio de variáveis de ambiente:

- `EMAIL_HOST`: Host do servidor SMTP
- `EMAIL_PORT`: Porta do servidor SMTP (padrão: `587`)
- `EMAIL_USERNAME`: Usuário de autenticação
- `EMAIL_PASSWORD`: Senha do usuário
- `EMAIL_FROM`: Endereço de e-mail do remetente

## Uso
Execute o script `email_automation.py` informando os destinatários que devem receber a mensagem. O exemplo abaixo envia um e-mail de teste para um destinatário:

```bash
python email_automation.py
```

Altere a lista de `recipients` no final do arquivo para definir seus próprios destinatários.

## Atenção
- Não compartilhe suas credenciais de e-mail publicamente.
- Verifique se o seu provedor de e-mail permite conexões SMTP e, se necessário, habilite senhas de apps ou configurações de acesso menos seguro.
