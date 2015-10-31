# coding=utf-8


class GamifyCommand(object):
    def __init__(self):
        self.data = {}

    def command(self, name):
        if name == 'frete_gratis':
            self.data['script'] = '''
                humane.log('Legal! Adicione mais um produto e você ganhará o frete grátis.', function() { callback(); });
            '''
        if name == 'cupom_desconto':
            self.data['script'] = '''
                humane.log('Parabéns! Você acaba de ganhar um cupom de desconto para a sua próxima compra.', function() { callback(); });
            '''
