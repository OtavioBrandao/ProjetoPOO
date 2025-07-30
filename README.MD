
# 🎬 **Video Streaming Service**

## 🚀 **Como Executar**

Para rodar o programa, execute o arquivo principal com o comando:

```bash
python main.py
```

---

## ✨ **Funcionalidades**

- 📚 **Consultar biblioteca de conteúdo** ✅
- 👤 **Configurações de usuário** ✅
- 🤖 **Recomendações personalizadas**
- 📱 **Streaming em múltiplos dispositivos**
- ⚡ **Otimização de banda larga**
- ⭐ **Marcar conteúdo e histórico de visualização** (50% feito)
- 📝 **Revisões e avaliações de conteúdo**
- 📢 **Integração com anúncios**
- 🔒 **Controle parental** ✅
- 👥 **Gerenciamento de usuário** ✅

---

## 📝 **Observações**

- 🔸 **Falta implementar a restrição de conteúdo no controle parental.**
- 🔸 **Falta restringir conteúdo conforme o plano do usuário**
- 🔸 **Adicionar uma forma de ver o pagamento enquanto aos planos**  
  (Premium: sem restrições e sem anúncios).

---

## 🏗️ **Estrutura de Projeto**

### 🏛️ **Classes:**

- **User**: Template para ministrar, administrar e utilizar diferentes usuários.
- **Perfil**: Template para diferentes perfis em cada usuário distinto.
- **ConjuntoMidias**: Template onde teremos todos os tipos de mídia possíveis e a partir delas realizar funções como explorar o conteúdo.
- **Midia**: Template que terá diversas outras subclasses referentes ao tipo de mídia, além de funções básicas como exibir informações de tal mídia.

  **Subclasses de Mídia:**
  - **Filme**: Para mídias que são filmes.
  - **Documentario**: Para mídias que são documentários.
  - **Serie**: Para mídias que são séries.
  - **Anime**: Para mídias que são animes.
  - **Novela**: Para mídias que são novelas.
  - **Historico**: Realiza o controle do histórico de exibição, permitindo funcionalidades como limpar histórico ou acessá-lo para cada perfil (vai ser um objeto de um atributo da classe Perfil).

- **Recomendacoes**: Template para sugerir conteúdos específicos baseado no gênero assistido pelo perfil (vai ser um objeto de um atributo da classe Perfil).
- **Anuncio**: Template para fazer a organização e manuntenção de anúncios na plataforma de acordo com o plano 
- **Marcar**: Template para marcar conteúdos específicos para assistir mais tarde e influenciar na recomendação do usuário
- **Plano**: Template para melhorar o gerenciamento de plano com pagamentos e ser utilizado no user_management, além de influenciar na parte dos anúncios devido ao plano escolhido com regras pre-estabelecidas;
- **Devices**: Template para a organização de streaming em multiplataforma;
- **BandaLarga**: Template para a manuntenção da banda larga e a qualidade da transmissão enquanto a pessoa assiste;
- **Avaliacoes**: Template para avaliações e reviews sobre um certo conteúdo em uma mini-rede social;