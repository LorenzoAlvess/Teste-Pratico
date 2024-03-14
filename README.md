# Teste de Desenvolvimento - Dashboard CRUD 💻

Bem-vindo(a) ao teste de desenvolvimento para a posição de estagiário! Este teste tem como objetivo avaliar suas habilidades na criação de uma Dashboard simples para uma biblioteca, incorporando dois CRUDs relacionados 1:N. A Dashboard deve fornecer informações essenciais, como **nome**, **data de criação** e incluir um pequeno gráfico para uma experiência visual mais rica.

## Objetivo 🚀

O objetivo deste teste é avaliar suas habilidades em:

1. **Desenvolvimento Front-end e UI/UX:** Criar uma interface de usuário intuitiva e simples para a Dashboard.

2. **Manipulação de Dados:** Implementar dois CRUDs relacionados 1:N, permitindo a criação, leitura, atualização e exclusão de itens.

3. **Visualização de Dados:** Integrar um pequeno gráfico que forneça insights visuais sobre os dados manipulados.

## Estrutura da Dashboard 📊

A Dashboard deve consistir em pelo menos duas seções principais:

### Seção 1: CRUD #1

- **Entidade:** Biblioteca
- **Campos:**
  - Nome
  - Data de Criação
  - Número de Livros Cadastrados
- **Operações:**
  - Adicionar
  - Visualizar Detalhes
  - Atualizar
  - Excluir

### Seção 2: CRUD #2 (Relacionado 1:N com CRUD #1)

- **Entidade:** Livros
- **Campos:**
  - Nome
  - Data de Criação
- **Operações:**
  - Adicionar
  - Visualizar Detalhes
  - Atualizar
  - Excluir

### Seção 3: Gráfico 📈

Integrar um gráfico simples que forneça uma representação visual dos dados. Use a biblioteca ou ferramenta de sua escolha (Seja Criativo!!).

## Como Executar ▶️

1. **Requisitos:** Certifique-se de ter os seguintes requisitos instalados em seu sistema:
   - Docker
   
2. **Instalação:** Siga os passos abaixo para iniciar a aplicação:
   - Clone o repositório:
     ```bash
     git clone https://github.com/LorenzoAlvess/Teste-Pratico.git
     ```
   - Acesse a pasta do projeto:
     ```bash
     cd dashboard
     ```
   - Crie o arquivo .env:
     - Copie o conteúdo do arquivo `.env.example` fornecido e salve-o como `.env` na pasta raiz dashboard.

3. **Execução:** Inicie a aplicação utilizando Docker:
   ```bash
   docker-compose up --build
