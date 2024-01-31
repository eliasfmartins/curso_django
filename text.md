separando componentes no django

primeiro por convencao cria se uma pasta chamada partials e outra chamada pages

que basicamente informa  que tipo de componente  tem dentro da pasta

seguindo vc cria o componente com os dados desejados

para incluir arquivos na pagina vc usa a tag include

{% include %} e o caminho do componente

exemplo em uso 

{}%include 'recipes/partials/head.html'%}
