# App de Relacionamentos com Mapa

Este projeto é um exemplo simples de uma aplicação de relacionamentos que
exibe usuários em um mapa (utilizando Leaflet e OpenStreetMap) e permite
curtir ou passar perfis, de forma semelhante ao Tinder.

## Estrutura

- `public/` contém os arquivos estáticos (HTML, CSS e JavaScript).
- `data/users.json` possui alguns usuários de exemplo com coordenadas.

## Como executar

1. Abra um terminal na pasta do projeto.
2. Utilize um servidor HTTP simples para servir os arquivos. Exemplo com
   Python:

   ```bash
   python3 -m http.server 8000
   ```

3. Acesse `http://localhost:8000/public/` no navegador.

## Funcionalidades

- Mapa exibindo a localização de cada usuário.
- Cartões de perfil com botões **Curtir** e **Passar**.

Este projeto é apenas um ponto de partida e pode ser expandido para incluir
autenticação, banco de dados e outras funcionalidades conforme necessário.
