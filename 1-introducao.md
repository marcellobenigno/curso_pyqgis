# 1.  Introdução ao PyQGIS

O PyQGIS é uma pacote python, que permite que você acesse e manipule o QGIS de diferentes formas, dentre elas, é possível:

* invocar comandos no console
* executar automaticamente um código python, quando o QGIS for inicializado
* criar ações customizadas
* criar novos algoritmos de processamento
* criar plugins e
* criar novas aplicações independentes (stand-alone) 

O QGIS foi escrito em C++, mas desde a versão 0.9 suporta a execução de scripts na linguagem Python.

### 1.1 Criando o seu primeiro programa:
 
Para acessar o console python, o usuário deve entrar no menu `plugins` e clicar em `python console`:

![](.pastes/2020-01-29-15-59-05.png)

Em seguida, abra o editor, clicando no botão da figura abaixo:

![](.pastes/2020-01-31-14-25-53.png)

Digite no editor o código:

```python
print('Olá Mundo')
```

E execute  o código, clicando no botão `Run Script`. O Resultado será visto na janela ao lado.