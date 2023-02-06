Projeto Django

Este projeto foi criado utilizando a versão 3.0.8 do Django, e tem como objetivo exemplificar a criação de um modelo de produto, seus serializers, viewsets e ações CRUD (Create, Read, Update, Delete).

Modelo de Produto
O modelo de produto é composto pelos seguintes campos:

Nome (CharField)
Preço (DecimalField)
Quantidade (PositiveIntegerField)
Peso (DecimalField)
Data de Expiração (DateField)
Desconto (DecimalField)
Marca (CharField)
Imagem (ImageField)
Serializers
O serializer do modelo de produto foi criado para ser utilizado com o Django Rest Framework. Ele permite a conversão do modelo em formato JSON e vice-versa.

Viewsets
O ViewSet foi criado para controlar as ações CRUD do modelo de produto. Ele permite a listagem, criação, atualização e exclusão dos produtos.

Ações CRUD
As ações CRUD foram criadas como views do Django Rest Framework. São elas:

Criação de Produto (Create)
Atualização de Quantidade de Produto (Update)
Exclusão de Produto (Delete)
Configurações do Django
As configurações gerais do projeto estão contidas no arquivo settings.py. Ele contém as configurações de segurança, aplicativos instalados, middlewares, URL's, entre outras. Além disso, é possível acessar as informações da documentação oficial do Django (https://docs.djangoproject.com/en/3.0/ref/settings/).

