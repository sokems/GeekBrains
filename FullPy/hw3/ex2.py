"""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку."""

old_str = 'Пауки — отряд членистоногих, первый по числу известных видов в ' \
          'классе паукообразных (ранее считался вторым после клещей, когда всех клещей объединяли в один отряд). ' \
          'Представители отряда распространены повсеместно. Пауки — облигатные хищники, питаются прежде всего ' \
          'насекомыми или другими мелкими животными. Известно лишь одно исключение — паук-скакун Bagheera kiplingi, ' \
          'питающийся зелёными частями акаций. Отряд включает около 50 тысяч современных и около 1 тысячи ' \
          'ископаемых видов. На территории бывшего СССР известно 2888 видов. Наука, изучающая пауков, ' \
          'называется арахнологией. Широко распространена боязнь пауков — арахнофобия.' \
          'Тело состоит из двух отделов: головогруди и в основном нерасчленённого брюшка[5], соединённых ' \
          'тонким стебельком (лат. petiolus s. pediculus), обыкновенно коротким, реже значительно ' \
          'удлинённым (у родов Myrmecium, Formicinoides); головогрудь бороздкой разделена на две ' \
          'явственные области: головную и грудную; из них первая несёт две пары конечностей: хелицеры ' \
          '(chelicerota, chelae, mandibulae), состоящие из одного толстого, обыкновенно короткого членика,' \
          ' вооружённого подвижным коготком, близ острия которого имеется отверстие канала, выводящего ядовитое ' \
          'выделение желез, находящихся в основном членике, и педипальпы (palpi), состоящие из 6 члеников (coxa, ' \
          'trochanter, femur, patella, tibia и tarsus). У половозрелых самцов тарсус педипальп превращён в совокупительный ' \
          'аппарат — цимбиум. Между хелицерами на вершине бугорка (rostrum) находится ротовое отверстие, ' \
          'служащее для сосания; этот бугорок снизу ограничен передним отростком груди (sternum), так ' \
          'называемой губой (pars labialis), а по бокам двумя максиллярными пластинками (lamina maxillares). ' \
          'Позади педипальп к головогруди прикреплены четыре пары ног, из которых каждая состоит из 7 члеников: ' \
          'тазика (соха), вертлуга (trochanter), бедра (femur), чашечки (patella), голени (tibia), предлапки ' \
          '(metatarsus) и лапки (tarsus), вооружённой снизу гладкими или зазубренными коготками, между которыми ' \
          'имеется иногда более короткий непарный коготок.'

old_str = old_str.lower()
old_list = []
new_list = []
double_dict = {}
res_dict = {}
punc = '''!()—-[]{};:'"\,<>./?@#$%^&*_~'''

for elem in old_str:
    if elem in punc or elem.isdigit():
        old_str = old_str.replace(elem, "")

old_list = old_str.split(' ')

for item in old_list:
    if item == '' or len(item) == 1:
        pass
    else:
        if item in new_list:
            if item in double_dict:
                double_dict[item] += 1
            else:
                double_dict[item] = 2
        else:
            new_list.append(item)

double_dict = sorted(double_dict.items(), key=lambda item: item[1], reverse=True)

while len(double_dict) > 10:
    double_dict.pop()

print(dict(double_dict))