# Computação Distribuída - Configuração do WordPress com Múltiplas Instâncias

Este repositório contém a entrega do Trabalho 2, que tem como objetivo executar múltiplas instâncias do WordPress utilizando o Nginx como balanceador de carga e o Docker Compose para orquestração dos contentores.

## Arquitetura
A infraestrutura é composta por 5 contentores:
*   1x Nginx (Balanceador de carga recebendo tráfego na porta 80).
*   3x WordPress (Instâncias da aplicação partilhando o volume `/var/www/html`).
*   1x MySQL (Banco de dados isolado na rede backend).

## Evidências e Análise de Funcionamento

### 1. Inicialização da Infraestrutura
Através do terminal, o comando `docker-compose up -d` foi executado para descarregar as imagens e iniciar os serviços. A interface do Docker Desktop confirmou que os contentores foram criados e encontram-se em execução estável.

### 2. Teste de Balanceamento via Terminal (CLI)
Para verificar a distribuição de carga pelo Nginx, foi executado o comando `curl.exe -I http://localhost/` múltiplas vezes consecutivas. 
A análise dos cabeçalhos HTTP devolvidos comprova o sucesso do balanceamento, uma vez que a variável `X-Upstream` alternou os endereços IP de resposta, encaminhando as requisições de forma circular para os três contentores do WordPress:
*   Resposta 1: `X-Upstream: 172.18.0.2:80`
*   Resposta 2: `X-Upstream: 172.18.0.3:80`
*   Resposta 3: `X-Upstream: 172.18.0.4:80`

### 3. Acesso e Teste via Navegador (Web)
O acesso via browser ao endereço `http://localhost/` redirecionou corretamente para a página de instalação do WordPress (`install.php`).
Utilizando as ferramentas de programador do navegador (DevTools > Network), a inspeção dos pacotes de rede confirmou o mesmo comportamento observado no terminal: ao recarregar a página, os "Cabeçalhos de Resposta" (Response Headers) do documento principal exibem o IP do contentor a alterar dinamicamente na propriedade `X-Upstream` (ex: alternando entre `172.18.0.3:80` e `172.18.0.2:80`).

Isto atesta que o Nginx está configurado corretamente como proxy reverso e a balancear a carga entre as instâncias da aplicação.