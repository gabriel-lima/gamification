def populate_storage():

    from website import scene_gateway
    from core import SceneStruct
    scene_gateway.save(SceneStruct(name='Cenario de exemplo de adicionou produtos',
                                   description='Cenario de exemplo, demonstrando como detectar a acao do usuario adicionar produtos ao carrinho de compras.',
                                   storage_xml='<xml xmlns="http://www.w3.org/1999/xhtml"><block type="controls_if" x="9" y="3"><value name="IF0"><block type="logic_compare"><field name="OP">EQ</field><value name="A"><block type="property_event" editable="false"></block></value><value name="B"><block type="event_adicionou_no_carrinho" editable="false"><data>adicionou_no_carrinho</data></block></value></block></value><statement name="DO0"><block type="block_frete_gratis"></block></statement></block></xml>',
                                   script_python='''if event == "adicionou_no_carrinho": gamify.command('frete_gratis')'''))
