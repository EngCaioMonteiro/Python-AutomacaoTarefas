# Automação de tarefas e criação de bots com PyAutoGUI e Pandas

Este projeto automatiza o processo de preenchimento de um formulário na web com dados extraídos de um arquivo CSV, utilizando as bibliotecas Python `PyAutoGUI` e `Pandas`.

## Objetivo
O objetivo do projeto é demonstrar como automatizar tarefas repetitivas, como o preenchimento de formulários em um navegador web, utilizando programação Python. O código abre o navegador, acessa uma página de login, faz login, e utiliza dados de um arquivo CSV para preencher campos em um formulário web.

## Tecnologias Utilizadas
- Python 3
- [PyAutoGUI](https://pyautogui.readthedocs.io/): Automação de interações com a interface gráfica.
- [Pandas](https://pandas.pydata.org/): Manipulação e análise de dados tabulares.

## Pré-requisitos
1. Instale as dependências:
   ```bash
   pip install pyautogui pandas
   ```
2. Certifique-se de que o arquivo `produtos.csv` está no mesmo diretório do script. Este arquivo deve conter os dados a serem preenchidos no formulário, no seguinte formato:

   | codigo | marca  | tipo   | categoria  | preco_unitario | custo  | obs           |
   |--------|--------|--------|------------|----------------|--------|---------------|
   | 101    | Marca1 | Tipo1  | Categoria1 | 50.00          | 30.00  | Observação1   |
   | 102    | Marca2 | Tipo2  | Categoria2 | 70.00          | 50.00  | Observação2   |

## Como Executar
1. Abra o terminal e execute o script Python:
   ```bash
   python codigo.py
   ```
2. O script fará o seguinte automaticamente:
   - Abrirá o navegador Firefox.
   - Acessará a URL de login fornecida.
   - Inserirá as credenciais de login.
   - Preencherá o formulário utilizando os dados do arquivo `produtos.csv`.

## Notas Importantes
- **Coordenadas de Tela**: As coordenadas usadas no código (`pyautogui.click(x, y)`) podem variar dependendo da resolução do monitor e do layout da interface. É necessário ajustar as coordenadas para seu ambiente.
- **Tempo de Espera**: O script utiliza `time.sleep()` para garantir que o carregamento das páginas e interações sejam realizados corretamente. Ajuste os tempos se necessário.
- **Segurança**: Evite incluir senhas diretamente no código. Considere usar variáveis de ambiente para maior segurança.

## Possíveis Melhorias
- Tornar as coordenadas dinâmicas utilizando técnicas de detecção de elementos, como OCR (Reconhecimento Óptico de Caracteres).
- Adicionar logs para monitorar o progresso da automação.
- Implementar suporte para múltiplos navegadores usando bibliotecas como Selenium.

## Autor
Este projeto foi desenvolvido por Caio Oliveira Monteiro em 2025, com base no código apresentado na aula pública da Jornada Python da Hashtag.

## Agradecimentos
Este projeto foi adaptado com base no código apresentado na aula pública da Jornada Python da Hashtag com o João Paulo de Lira. As adaptações foram realizadas para personalizar o uso para [navegador Mozilla Firefox, entre outros ajustes].

## Licença
Este projeto está disponível sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.

---

Divirta-se automatizando! 😊
