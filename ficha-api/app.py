from flask import Flask, jsonify, request


app = Flask(__name__)

fichas = [
        {      
                'id': 1,
                'status': 'Solicitado',
                'solicitante':{
                        'id': 10,
                        'nome':'Luiz Claudio Ferreira',
                        'telefone':'82966666666',
                        'email':'luiz.claudio@ufal.br',
                        'nivel':{
                                'id': 2,
                                'descricao': 'Mestrado'
                                 },
                        'curso': {
                                'id': 2,
                                'descricao':'Modelagem Computacional de Conhecimento'
                                },
                        'instituicao': {
                                'id': 1,
                                'descricao': 'Universidade Federal de Alagoas',
                                'sigla': 'UFAL'
                                },
                        'unidade': {'id': 2,
                                    'descricao': 'Centro de Educação',
                                    'sigla': 'CEDU'
                                   },
                        'campus': {'id': 1,
                                   'descricao': 'Campus A. C. Simões (Maceió)'
                                  }
                        },
                'autores': [
                        {
                        'nome': 'Luiz Cláudio Ferreira da',
                        'sobrenome': 'Silva Júnior'
                        }
                 ],
                'orientador': {
                        'nome': 'Fernando',
                        'sobrenome': 'Pimentel'
                        },
                'titulo':'Novas Tecnologias Digitais na Educação',
                'subtitulo':'reflexões sobre o uso na sala de aula',
                'resumo':'Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se o desenvolvimento contínuo de distintas formas de atuação faz parte de um processo de gerenciamento da gestão inovadora da qual fazemos parte. O cuidado em identificar pontos críticos no fenômeno da Internet facilita a criação dos métodos utilizados na avaliação de resultados. Do mesmo modo, a percepção das dificuldades não pode mais se dissociar dos níveis de motivação departamental. No entanto, não podemos esquecer que a revolução dos costumes promove a alavancagem do fluxo de informações. Assim mesmo, o novo modelo estrutural aqui preconizado representa uma abertura para a melhoria das posturas dos órgãos dirigentes com relação às suas atribuições. A prática cotidiana prova que o comprometimento entre as equipes prepara-nos para enfrentar situações atípicas decorrentes do impacto na agilidade decisória. É claro que o entendimento das metas propostas cumpre um papel essencial na formulação do sistema de formação de quadros que corresponde às necessidades.',
                'folhas':'250',
                'ilustracao':'Sim',
                'local':'Maceió',
                'ano_defesa':'2019',
                'assuntos': ['Educação','Tecnologia da Informação e Comunicação'],
                'documento': 'http://www.drive.com/meutrabalho.pdf'
        },
        {      
                'id': 2,
                'status': 'Solicitado',
                'solicitante':{
                        'id': 20,
                        'nome':'Lucas Cezar',
                        'telefone':'82999999999',
                        'email':'lucas@cezar.com.br',
                        'nivel':{
                                'id': 1,
                                'descricao': 'Graduação'
                                 },
                        'curso': {
                                'id': 1,
                                'descricao':'Computação'
                                },
                        'instituicao': {
                                'id': 1,
                                'descricao': 'Universidade Federal de Alagoas',
                                'sigla': 'UFAL'
                                },
                        'unidade': {'id': 1,
                                    'descricao': 'Instituto de Computação',
                                    'sigla': 'IC'
                                   },
                        'campus': {'id': 1,
                                   'descricao': 'Campus A. C. Simões (Maceió)'
                                  }
                },
                'autores': [
                        {
                        'nome': 'Lucas Cezar',
                        'sobrenome': 'Moraes'
                        },
                        {
                        'nome': 'Luiz Cláudio Ferreira',
                        'sobrenome': 'Silva Júnior'
                        },
                 ],
                'orientador': {
                        'nome': 'Ig',
                        'sobrenome': 'Bittencourt'
                        },
                'coorientador': {
                        'nome': 'Alan Pedro da',
                        'sobrenome': 'Silva'
                        },
                'titulo':'Gamificação na Educação',
                'subtitulo':'',
                'resumo':'Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se o desenvolvimento contínuo de distintas formas de atuação faz parte de um processo de gerenciamento da gestão inovadora da qual fazemos parte. O cuidado em identificar pontos críticos no fenômeno da Internet facilita a criação dos métodos utilizados na avaliação de resultados. Do mesmo modo, a percepção das dificuldades não pode mais se dissociar dos níveis de motivação departamental. No entanto, não podemos esquecer que a revolução dos costumes promove a alavancagem do fluxo de informações. Assim mesmo, o novo modelo estrutural aqui preconizado representa uma abertura para a melhoria das posturas dos órgãos dirigentes com relação às suas atribuições. A prática cotidiana prova que o comprometimento entre as equipes prepara-nos para enfrentar situações atípicas decorrentes do impacto na agilidade decisória. É claro que o entendimento das metas propostas cumpre um papel essencial na formulação do sistema de formação de quadros que corresponde às necessidades.',
                'folhas':'150',
                'ilustracao':'Sim',
                'local':'Maceió',
                'ano_defesa':'2018',
                'assuntos': ['Educação','Aprendizagem','Gamificação'],
                'documento': 'http://www.drive.com/trabalholucas.pdf'
        }                
]

@app.route('/fichas', methods=['GET'])
def home():
    return jsonify(fichas), 200


@app.route('/fichas/<string:unidade>', methods=['GET'])
def fichas_por_unidade(unidade):
    fichas_por_unidade = [ficha for ficha in fichas if ficha['solicitante']['unidade']['descricao'] == unidade]
    if fichas_por_unidade:
        return jsonify(fichas_por_unidade), 200
    return jsonify({'error': 'not found'}), 404

    
@app.route('/fichas/<int:id>', methods=['GET'])
def fichas_por_id(id):
    for ficha in fichas:
        if ficha['id'] == id:
            return jsonify(ficha), 200

    return jsonify({'error': 'not found'}), 404
    

@app.route('/fichas', methods=['POST'])
def save_ficha():
    data = request.get_json()
    fichas.append(data)
    
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)