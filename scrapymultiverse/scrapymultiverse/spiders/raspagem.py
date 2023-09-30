import scrapy

class ImageSpider(scrapy.Spider):
    name = 'image_spider'
    start_urls = [
        'https://multiversocomicon.com.br/',
    ]

    def parse(self, response):
        # Extrair links das imagens
        image_urls = response.css('style data-bsrjs').extract()

        # Iterar sobre os links das imagens
        for img_url in image_urls:
            # Baixar a imagem e especificar o nome do arquivo
            yield scrapy.Request(url=img_url, callback=self.save_image)

    def save_image(self, response):
        # Extrair o nome da imagem do URL
        image_name = response.url.split('/')[-1]

        # Especificar o diretório onde as imagens serão salvas
        save_path = 'G:/Users/raphael/automacaopy/automacao-py/imagens teste' + image_name

        # Salvar a imagem no diretório especificado
        with open(save_path, 'wb') as f:
            f.write(response.body)