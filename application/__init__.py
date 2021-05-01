from flask import Flask
import os
from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia

app = Flask(__name__, static_folder = os.path.abspath("application/view/static"), template_folder = os.path.abspath("application/view/templates"))

noticia1 = Noticia("noticia1_rj.jfif", "Covid19 - 1", "texto1", "30/04/2021", 1, 19537835, 215463)
noticia2 = Noticia("noticia2_rj.jpg", "Covid19 - 2", "texto2", "30/04/2021", 2, 82734657, 363456)
noticia3 = Noticia("noticia3_sp.jpg", "Covid19 - 3", "texto3", "30/04/2021", 3, 76354743, 321542)
noticia4 = Noticia("noticia4_sp.jpg", "Covid19 - 4", "texto4", "30/04/2021", 4, 62643566, 677265)

noticia1.set_titulo("Prefeitura do Rio prorroga restrições contra Covid-19 até 10 de maio")
noticia1.set_texto("A prefeitura do Rio do Rio de Janeiro prorrogou até 10 de maio as medidas restritivas de isolamento social contra a disseminação da Covid-19, mostrou decreto publicado no Diário Oficial do município nesta sexta-feira. <br> O acesso às praias para banho de sol e de mar segue proibido aos fins de semana, apesar dos flagrantes de desrespeito à medida no último fim de semana. O toque de recolher, em que as pessoas são proibidas de ficar nas ruas entre 23h e 5h, também foi mantido. <br> Comércio e serviços seguem liberados para operar em horários e condições especiais.")
noticia1.set_url_noticia("https://www.terra.com.br/noticias/brasil/prefeitura-do-rio-prorroga-restricoes-contra-covid-19-ate-10-de-maio,a15d4d43404e9d3c81db9138bf96f6bbfu33nirm.html")

noticia2.set_titulo("RJ registra maior número de mortes por Covid em um mês desde o início da pandemia")
noticia2.set_texto("O Estado do Rio registrou em abril deste ano o maior número de mortes causadas pela Covid em um mês desde o início da pandemia no país. Foram 6.788 óbitos causados pela doença até a tarde desta sexta-feira (30), segundo dados do Portal da Transparência do Registro Civil. Até o momento, maio de 2020 era o mês com mais mortes relacionados à Covid-19 - foram 6.778 óbitos.")
noticia2.set_url_noticia("https://g1.globo.com/rj/rio-de-janeiro/noticia/2021/04/30/rj-registra-maior-numero-de-mortes-por-covid-em-um-mes-desde-o-inicio-da-pandemia.ghtml")

noticia3.set_titulo("SP encerra abril com queda de 29% nas internações por COVID-19")
noticia3.set_texto("O número representa 9.306 internações a menos se comparado ao último dia de março (31), que atingiu 31.175 internações nessa data. Desde o início da pandemia, houve 2.903.709 casos e 96.191 óbitos. Entre o total de casos, 2.552.653 tiveram a doença e já estão recuperados, sendo que 296.730 foram internados e receberam alta hospitalar. A taxa de ocupação dos leitos de UTI no estado é de 79,1% e na Grande São Paulo é de 77,3%.")
noticia3.set_url_noticia("https://www.saopaulo.sp.gov.br/noticias-coronavirus/sp-encerra-abril-com-queda-de-29-nas-internacoes-por-covid-19/")

noticia4.set_titulo("Justiça Federal em SP determina que governo federal pare de fazer campanhas do 'kit Covid'")
noticia4.set_texto("A Justiça Federal em São Paulo determinou que o governo federal pare de fazer campanhas com referências a medicamentos sem eficácia comprovada contra a Covid-19 e que os influenciadores digitais contratados pela gestão publiquem mensagens para desencorajar o uso do 'kit Covid'. A decisão da juíza Ana Lúcia Petri Betto, da 6ª Vara Cível Federal de São Paulo, é de quinta-feira (29), mas foi divulgada nesta sexta-feira (30). Ela atende a uma ação civil pública protocolada por Luna Zarattini Brandão, que foi candidata a vereadora na capital paulista pelo Partido dos Trabalhadores, contra o ex-secretário de Comunicação da Presidência Fabio Wajngarten, e contra a agência Calia/Y2 Propaganda e Marketing e os influenciadores Flavia Viana, João Zoli, Jessica Tayara e Pam Puertas.")
noticia4.set_url_noticia("https://g1.globo.com/sp/sao-paulo/noticia/2021/04/30/justica-federal-em-sp-determina-que-governo-federal-pare-de-fazer-campanhas-do-kit-covid.ghtml")

noticia_lista = [noticia1, noticia2, noticia3, noticia4]

estado_lista = []

estado1 = Estado("Rio de Janeiro", "RJ", "bandeira_rj.png", 1, [noticia1, noticia2])
estado2 = Estado("São Paulo", "SP", "bandeira_sp.png", 2, [noticia3, noticia4])

estado_lista = [estado1, estado2]

from application.controller import home_controller