# Keylogger
Este é um código de keylogger em Python, usando as bibliotecas pynput.mouse e pynput.keyboard. Um keylogger é um programa que registra todas as teclas pressionadas em um computador sem o conhecimento ou consentimento do usuário, permitindo que as informações sejam armazenadas em um arquivo de log.

## Bibliotecas Usadas
- pynput.mouse: É uma biblioteca que permite monitorar eventos do mouse, como cliques e movimentos.
- pynput.keyboard: É uma biblioteca que permite monitorar eventos do teclado, como teclas pressionadas e liberadas.
- pyautogui: É uma biblioteca do Python para automação de tarefas relacionadas à interface gráfica do usuário.

## Funcionamento

- O código cria um diretório com base na data atual na pasta desejada, onde serão armazenados os arquivos de log.
- Os eventos do mouse são monitorados pelo listener MouseListener que chama a função on_click sempre que um botão do mouse é pressionado. A função on_click tira um screenshot da tela e salva em um arquivo com um nome baseado no horário em que o evento ocorreu.
- Os eventos do teclado são monitorados pelo listener KeybordListener que chama a função on_press sempre que uma tecla é pressionada. A função on_press formata a tecla pressionada removendo caracteres indesejados e substituindo alguns códigos especiais.
- A tecla pressionada é registrada em um arquivo de log com base no caminho do diretório criado anteriormente.
- Se a tecla pressionada for a tecla de backspace, o log é atualizado para remover o último caractere registrado, simulando a função de apagar.
- Os listeners são iniciados e o código fica em execução para monitorar continuamente os eventos do mouse e do teclado.
- O programa pode ser interrompido manualmente, encerrando a execução do código.

## Considerações finais

É importante observar que o uso de keyloggers pode ser ilegal sem o consentimento expresso do usuário. Portanto, é fundamental garantir que o uso deste código esteja em conformidade com as leis locais e as políticas de privacidade aplicáveis.
