
# PrintBot

## Sobre

Aplicação desenvolvida para automação de envio de impressões atraves de uma pasta compartilhada. Linguagem escolhida para a resolução Python. Script desenvolvido para resolver um problema especifico de necessidade de realizar envio de arquivos PDF para a impressora de qualquer computador sem necessidade de instalar o drive. 


## Como o Script funciona

## Pré-requisitos.
- Windows
- python 3.10
- pywin32
- Foxit

## Instalações

* O Python 3 no Windows - http://python.org.br/instalacao-windows/
    * dependencia python pywin32  
    
            pip install pywin32

* Foxit 

    * Baixe o pacote de instalação neste link https://www.foxit.com/pt-br/downloads/ e instale no Windows 
    * Adicione o Foxit como programa padrão do sistema
## Compartilhamento de pasta
    1. Compartilhando pastas em ambiente Windows
    2. Localize a pasta que será compartilhada e clique com o botão direito do mouse;
    3. Escolha "compartilhar com ..." ou “conceder acesso a..” ou selecione "pessoas específicas";
    4. Identifique o usuário, grupo de usuários ou aplicativo que terá permissão para acessar esse conteúdo.

## Como Utilizar

* Se tudo estiver devidamente configurado basta colocar um arquivo .PDF na pasta que automaticamente o script enviara o arquivo para a impressora
