from flask import Flask, render_template, request

# Cria uma instância da aplicação Flask
app = Flask(__name__)


# Cria uma rota '/' e autoriza o métodos GET e POST
@app.route('/', methods=['GET', 'POST'])

# Define a função que será chamada quando a rota '/' for acessada
def index():
    expression = '' # inicializa a variável como uma stirng vazia. Essa variável armazenará a expressão matemática
    
    if request.method == 'POST': # Verifica se o tipo de requisição feita na rota é do tipo POST
        expression = request.form.get('expression', '') # Obtém o valor do campo expression do formulário. Se o campo não existir, usa uma string vazia como padrão.
        button = request.form.get('button', '') # Obtém o valor do campo button do formulário. Se o campo não existir, usa uma string vazia como padrão.
        print(f"Button: {button}, Expression: {expression}") # Imprime no console o valor do botão pressionado e a expressão atual para depuração.

        if button == '=':
            try:
                expression = expression.replace('÷', '/').replace('×', '*')  # Substitui os caracteres especiais ÷ e × por / e * para que a expressão seja corretamente interpretada pelo eval().
                result = eval(expression)
                expression = str(result) # Converte o resultado da avaliação para uma string e atualiza a variável expression.
            except Exception as e:
                print(f"Error: {e}")
                expression = 'Error' # Se houver um erro, a expressão é definida como 'Error'
        elif button == 'C':
            expression = '' # Se o botão de limpar foi pressionado, redefine a expressão para uma string vazia.
        else: # Para qualquer outro botão que não seja = ou C, executa o bloco abaixo.
            if button in '0123456789+-*/().': # Verifica se o botão pressionado é um caractere válido para uma expressão matemática.
                expression += button # Adiciona o caractere do botão pressionado à expressão atual.
        
        return render_template('index.html', expression=expression) # Renderiza o template index.html e passa a variável expression para o template. Isso atualiza a tela com a nova expressão ou resultado.
    
    return render_template('index.html', expression='') # Quando a requisição é do tipo GET, exibe a calculadora limpa

if __name__ == '__main__':
    app.run(debug=True)


