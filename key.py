from dataclasses import dataclass

matrizindice = ["[0][0]"]
matriztexto = ["Asas bem desenvolvidas, um ou dois pares."]

matrizindice.append("[1][0]")
matrizindice.append("[2][0]")
matrizindice.append("[3][0]")
matrizindice.append("[4][0]")
matrizindice.append("[3][1]")
matrizindice.append("[4][2]")
matrizindice.append("[5][4]")
matrizindice.append("[4][3]")
matrizindice.append("[5][6]")
matrizindice.append("[2][1]")
matrizindice.append("[3][2]")
matrizindice.append("[4][4]")
matrizindice.append("[5][8]")
matrizindice.append("[6][16]")
matrizindice.append("[5][9]")
matrizindice.append("[6][18]")
matrizindice.append("[7][36]")
matrizindice.append("[6][19]")
matrizindice.append("[7][38]")
matrizindice.append("[8][76]")
matrizindice.append("[4][5]")
matrizindice.append("[5][10]")
matrizindice.append("[7][39]")
matrizindice.append("[8][78]")
matrizindice.append("[3][3]")
matrizindice.append("[4][6]")
matrizindice.append("[5][12]")
matrizindice.append("[4][7]")
matrizindice.append("[5][14]")
matrizindice.append("[6][28]")
matrizindice.append("[5][15]")
matrizindice.append("[6][30]")
matrizindice.append("[1][1]")
matrizindice.append("[2][2]")
matrizindice.append("[3][4]")
matrizindice.append("[4][8]")
matrizindice.append("[5][16]")
matrizindice.append("[4][9]")
matrizindice.append("[5][18]")
matrizindice.append("[3][5]")
matrizindice.append("[4][10]")
matrizindice.append("[5][20]")
matrizindice.append("[6][40]")
matrizindice.append("[5][21]")
matrizindice.append("[6][42]")
matrizindice.append("[4][11]")
matrizindice.append("[5][22]")
matrizindice.append("[6][44]")
matrizindice.append("[5][23]")
matrizindice.append("[6][46]")
matrizindice.append("[2][3]")
matrizindice.append("[3][6]")
matrizindice.append("[4][12]")
matrizindice.append("[3][7]")
matrizindice.append("[4][14]")
matrizindice.append("[5][28]")
matrizindice.append("[4][15]")
matrizindice.append("[5][30]")
matrizindice.append("[6][60]")
matrizindice.append("[5][31]")
matrizindice.append("[6][62]")
matrizindice.append("[7][124]")
matrizindice.append("[8][248]")
matrizindice.append("[7][125]")
matrizindice.append("[8][250]")
matrizindice.append("[9][500]")
matrizindice.append("[8][251]")
matrizindice.append("[9][502]")
matrizindice.append("[10][1004]")
matrizindice.append("[9][503]")
matrizindice.append("[10][1006]")
matrizindice.append("[11][2012]")
matrizindice.append("[10][1007]")
matrizindice.append("[11][2014]")
matrizindice.append("[12][4028]")
matrizindice.append("[11][2015]")
matrizindice.append("[12][4030]")
matrizindice.append("[6][63]")
matrizindice.append("[7][126]")
matrizindice.append("[8][252]")
matrizindice.append("[9][504]")
matrizindice.append("[10][1008]")
matrizindice.append("[9][505]")
matrizindice.append("[10][1010]")
matrizindice.append("[8][253]")
matrizindice.append("[9][506]")
matrizindice.append("[10][1012]")
matrizindice.append("[9][507]")
matrizindice.append("[10][1014]")
matrizindice.append("[11][2028]")
matrizindice.append("[10][1015]")
matrizindice.append("[11][2030]")
matrizindice.append("[12][4060]")
matrizindice.append("[11][2031]")
matrizindice.append("[12][4062]")
matrizindice.append("[13][8124]")
matrizindice.append("[12][4063]")
matrizindice.append("[13][8126]")
matrizindice.append("[7][127]")
matrizindice.append("[8][254]")
matrizindice.append("[9][508]")
matrizindice.append("[10][1016]")
matrizindice.append("[11][2032]")
matrizindice.append("[10][1017]")
matrizindice.append("[11][2034]")
matrizindice.append("[12][4068]")
matrizindice.append("[11][2035]")
matrizindice.append("[12][4070]")
matrizindice.append("[13][8140]")
matrizindice.append("[9][509]")
matrizindice.append("[10][1018]")
matrizindice.append("[12][4071]")
matrizindice.append("[13][8142]")
matrizindice.append("[8][255]")
matrizindice.append("[9][510]")
matrizindice.append("[10][1020]")
matrizindice.append("[9][511]")
matrizindice.append("[10][1022]")
matrizindice.append("[11][2044]")
matrizindice.append("[10][1023]")
matrizindice.append("[11][2046]")
matrizindice.append("[0][1]")
matrizindice.append("[1][2]")
matrizindice.append("[2][4]")
matrizindice.append("[3][8]")
matrizindice.append("[2][5]")
matrizindice.append("[3][10]")
matrizindice.append("[1][3]")
matrizindice.append("[2][6]")
matrizindice.append("[3][12]")
matrizindice.append("[2][7]")
matrizindice.append("[3][14]")
matrizindice.append("[4][28]")
matrizindice.append("[3][15]")
matrizindice.append("[4][30]")
matrizindice.append("[5][60]")
matrizindice.append("[6][120]")
matrizindice.append("[5][61]")
matrizindice.append("[6][122]")
matrizindice.append("[7][244]")
matrizindice.append("[6][123]")
matrizindice.append("[7][246]")
matrizindice.append("[4][31]")
matrizindice.append("[5][62]")
matrizindice.append("[6][124]")
matrizindice.append("[7][248]")
matrizindice.append("[8][496]")
matrizindice.append("[7][249]")
matrizindice.append("[8][498]")
matrizindice.append("[6][125]")
matrizindice.append("[7][250]")
matrizindice.append("[8][500]")
matrizindice.append("[7][251]")
matrizindice.append("[8][502]")
matrizindice.append("[5][63]")
matrizindice.append("[6][126]")
matrizindice.append("[7][252]")
matrizindice.append("[6][127]")
matrizindice.append("[7][254]")
matrizindice.append("[8][508]")
matrizindice.append("[7][255]")
matrizindice.append("[8][510]")
matrizindice.append("[9][1020]")
matrizindice.append("[8][511]")
matrizindice.append("[9][1022]")
matrizindice.append("[10][2044]")
matrizindice.append("[9][1023]")
matrizindice.append("[10][2046]")
matrizindice.append("[11][4092]")
matrizindice.append("[12][8184]")
matrizindice.append("[11][4093]")
matrizindice.append("[12][8186]")
matrizindice.append("[10][2047]")
matrizindice.append("[11][4094]")
matrizindice.append("[12][8188]")
matrizindice.append("[11][4095]")
matrizindice.append("[12][8190]")
matrizindice.append("[13][16380]")
matrizindice.append("[12][8191]")
matrizindice.append("[13][16382]")
matrizindice.append("[14][32764]")
matrizindice.append("[13][16383]")
matrizindice.append("[14][32766]")
matrizindice.append("[15][65532]")
matrizindice.append("[14][32767]")
matrizindice.append("[15][65534]")
matrizindice.append("[16][131068]")
matrizindice.append("[15][65535]")
matrizindice.append("[16][131070]")
matrizindice.append("[17][262140]")
matrizindice.append("[16][131071]")
matrizindice.append("[17][262142]")
matrizindice.append("[18][524284]")
matrizindice.append("[19][1048568]")
matrizindice.append("[18][524285]")
matrizindice.append("[19][1048570]")
matrizindice.append("[17][262143]")
matrizindice.append("[18][524286]")
matrizindice.append("[19][1048572]")
matrizindice.append("[18][524287]")
matrizindice.append("[19][1048574]")
matrizindice.append("[20][2097148]")
matrizindice.append("[19][1048575]")
matrizindice.append("[20][2097150]")

# 1
matriztexto.append(
    "Asa anterior endurecida ou coriácea (élitro), coriácea na parte basal e membranosa na distal. (hemiélitro) ou pergaminosa (tégmina). Asa posterior membranosa, quando presente.")

matriztexto.append(
    "Asa anterior coriácea (élitro), sem veias, às vezes com estrias paralelas que podem fundir-se posteriormente.")
matriztexto.append(
    "Asa anterior claviforme, diminuta. Asa posterior membranosa, sempre expandida, em forma de leque. Antena com quatro a sete artículos e pelo menos um flagelômero flabelado (apêndice lateral longo). Espécimes com menos de 5 mm de comprimento (machos de estrepsípteros).")
# ordem
matriztexto.append("Strepsiptera")
matriztexto.append(
    "Asa anterior nunca claviforme. Asa posterior oculta sob o élitro, geralmente com dobras transversais ou longitudinais.")
matriztexto.append(
    "Cerco em forma de pinça. Antena longa, geralmente com mais de 12 artículos, delgada. Asa anterior coriácea, curta, deixando a maior parte do abdômen exposto. Asa posterior membranosa, em repouso dobrada sob a asa anterior, quando expandida, de forma semicircular, com dobras radiais em forma de leque (tesourinhas, lacrainhas).")
# ordem
matriztexto.append("Dermaptera")
matriztexto.append(
    "Cerco ausente. Se estrutura em forma de pinça estiver presente, então a asa anterior cobre a maior parte do abdômen. Élitro variável em comprimento. Antena com 11 artículos ou menos. Asa posterior alongada, com dobras longitudinais ou transversais (besouros).")
# ordem
matriztexto.append("Coleoptera")
matriztexto.append(
    "Asa anterior coriácea na base (hemiélitro) ou pergaminosa (tégmina), quase sempre com veias ramificadas.")
matriztexto.append(
    "Aparelho bucal mastigador. Mandíbula com movimentos no plano horizontal.")
matriztexto.append(
    "Asa posterior mais larga que a anterior, com dobras longitudinais em forma de leque.")
matriztexto.append(
    "Pronoto com lobo lateral descendente bem desenvolvido. Perna posterior quase sempre modificada para o salto, com fêmur engrossado. Fêmur e tíbia posteriores mais longos do que os respectivos segmentos das pernas anterior e média. Se pernas posterior e média semelhantes, então corpo subcilíndrico e perna anterior fossorial. Muitos produzem sons (gafanhotos, grilos, esperanças, paquinhas).")
# ordem
matriztexto.append("Orthoptera")
matriztexto.append(
    "Pronoto sem lobo lateral descendente bem desenvolvido. Perna posterior não modificada para o salto. Se maior que a perna média, então o fêmur não é engrossado. Se perna anterior fossorial, então corpo ovalado e achatado dorsoventralmente. Incapazes de produzir sons ou produzindo somente chiados.")
matriztexto.append(
    "Corpo largo, achatado dorso-ventralmente. Cabeça quase ou totalmente oculta pelo pronoto em vista dorsal. Pernas curtas e fortes, subiguais na forma e no tamanho, com as tíbias espinhosas (baratas).")
# ordem
matriztexto.append("Blattaria")
matriztexto.append(
    "Corpo geralmente estreito, alongado. Cabeça exposta. Pernas delgadas, anteriores geralmente mais longas, às vezes raptoriais. Tíbias sem espinhos.")
matriztexto.append(
    "Perna anterior raptorial. Protórax geralmente mais longo que o mesotórax. Cerco com vários articulas (louva-a-deus, põe-mesa).")
# ordem
matriztexto.append("Mantodea")
matriztexto.append(
    "Asa posterior um tanto semelhante à anterior, sem dobras longitudinais. Asa anterior com base esclerosada separada do restante por uma linha de fraqueza, que permite a quebra da asa (cupins, siriris, aleluias, térmitas).")
# ordem
matriztexto.append("Isoptera")
matriztexto.append(
    "Perna anterior não raptorial. Protórax mais curto do que o mesotórax. Cerco com um articulo (bichos-paus, bichos-graveto).")
# ordem
matriztexto.append("Phasmatodea")
matriztexto.append(
    "Aparelho bucal sugador, em forma de rostro (tubo adaptado para sugar), geralmente alongado, surgindo da parte ventral da cabeça e geralmente dirigido para trás. Palpo maxilar e labial ausentes (pulgões, cochonilhas, cigarras, cigarrinhas, percevejos, baratas d'água) - Ordem Hemiptera - ir até subordem.")
matriztexto.append(
    "Rostro originando-se na região anterior da cabeça, com três ou quatro artículos quando três, nunca ultrapassando o primeiro par de coxas. Antena com quatro ou cinco artículos, nunca cerdiforme. Asa anterior geralmente com a metade basal coriácea e a metade distai membranosa (hemiélitro), plana sobre o abdômen, a parte membranosa sobrepondo-se quando em repouso (percevejos).")
# ordem - Ordem
matriztexto.append("Heteroptera")
matriztexto.append(
    "Rostro originando-se na região posterior da cabeça ou aparentemente entre as coxas anteriores, sempre com três artículos. Antena cerdiforme ou com mais de cinco articulas. Asa anterior de textura uniforme, pergaminácea (tégmina), às vezes membranosa, geralmente tectiforme.")
matriztexto.append(
    "Tarsos trímeros. Flagelo geralmente curto, cerdiforme. Rostro saindo da parte posterior da cabeça. Venação geralmente bem desenvolvida. Insetos de vida livre (cigarras, cigarrinhas).")
# ordem
matriztexto.append("Auchenorryncha")
matriztexto.append(
    "Tarsos mono ou dímeros. Flagelo geralmente longo, filiforme, com articulação distinta, nunca com menos de seis articulas. Rostro, quando presente, saindo entre as coxas anteriores. Venação reduzida. Insetos geralmente fixos ao substrato (pulgões, cochonilhas, psilídeos).")
# ordem
matriztexto.append("Sternorrhyncha")
matriztexto.append(
    "Asa anterior membranosa, às vezes coberta de escamas. Asa posterior, quando presente, semelhante à textura da asa anterior.")
matriztexto.append(
    "Com um par de asas, segundo par às vezes transformado em halter (balancim).")
matriztexto.append(
    "Ápice do abdômen com um a três filamentos longos. Aparelho bucal vestigial.")
matriztexto.append(
    "Asa anterior com várias veias e células. Asa posterior pequena ou ausente. Antena curta, cerdiforme, inconspícua. Abdômen com dois ou três filamentos caudais longos. Geralmente mais de 5 mm de comprimento (efeméridas).")
# ordem
matriztexto.append("Ephemeroptera")
matriztexto.append(
    "Asa anterior com uma ou duas veias. Asa posterior modificada, semelhante a um halter em forma de gancho. Antena longa, conspícua. Ápice do abdômen com um filamento mediano longo. Geralmente menos de 5 mm de comprimento (machos de cochonilhas) (Coccoidea).")
matriztexto.append("Sternorrhyncha")
matriztexto.append(
    "Ápice do abdômen sem filamentos longos. Aparelho bucal geralmente bem desenvolvido, com mandíbulas ou rostro.")
matriztexto.append(
    "Halter (balancim) presente. Aparelho bucal geralmente sugador ou vestigial se mandíbula presente, então corpo com menos de 1 mm de comprimento. Palpo maxilar presente. Protórax geralmente muito reduzido e fundido ao mesotórax, este bastante desenvolvido. Tarsos geralmente pentâmeros.")
matriztexto.append(
    "Base do abdômen com pecíolo bissegmentado. Asa franjada com cerdas longas. Aparelho bucal com mandíbula. Menos de 1 mm de comprimento (Mymarommatidae).")
# ordem
matriztexto.append("Hymenoptera")
matriztexto.append(
    "Base do abdômen normal se peciolada, sem segmentação. Asa sem franja de cerdas longas. Aparelho bucal sugador ou vestigial. Geralmente mais de 1 mm de comprimento (moscas, mosquitos).")
# ordem
matriztexto.append("Diptera")
matriztexto.append(
    "Halter ausente. Aparelho bucal com mandíbula ou sem palpo maxilar. Protórax bem separado do mesotórax, conspícuo. Tarsos dímeros ou trímeros.")
matriztexto.append(
    "Aparelho bucal com mandíbula. Antena longa e conspícua, com 13 artículos ou mais. Palpo maxilar e labial presentes.")
# ordem
matriztexto.append("Psocoptera")
matriztexto.append(
    "Aparelho bucal sugador, em forma de rostro. Antena curta, cerdiforme, com menos de 11 artículos. Palpo maxilar e labial ausentes (alguns Fulgoroidea).")
# ordem
matriztexto.append("Auchenorryncha")
matriztexto.append("Com dois pares de asas.")
matriztexto.append(
    "Asas anterior e posterior total ou parcialmente cobertas por escamas. Aparelho bucal geralmente espiralado (espirotromba), raramente vestigial (borboletas, mariposas).")
# ordem
matriztexto.append("Lepidoptera")
matriztexto.append("Asas sem escamas. Aparelho bucal não espiralado.")
matriztexto.append(
    "Asas longas, estreitas, com duas veias ou menos, franjadas, com cerdas longas nas margens. Tarsos mono ou dímeros. Menos de 5 mm de comprimento (tripes, lacerdinhas)")
# ordem
matriztexto.append("Lepidoptera")
matriztexto.append(
    "Asas largas, com várias veias se alongada, então tarsos com mais de dois artículos.")
matriztexto.append(
    "Asa anterior relativamente grande. Asa posterior pequena, subarredondada. Asas veias transversais formando células, quando em descanso, mantidas juntas sobre o corpo. Antena curta, cerdiforme. Abdômen com dois ou três filamentos caudais longos, multiarticulados (efeméridas).")
# ordem
matriztexto.append("Ephemeroptera")
matriztexto.append("Com outra combinação de caracteres.")
matriztexto.append("Tarsos pentâmeros.")
matriztexto.append(
    "Asa anterior distintamente revestida com cerdas. Aparelho bucal atrofiado, exceto o palpo labial e o maxilar, geralmente bem desenvolvidos. Antena longa, pelo menos tão longa quanto o comprimento do corpo.")
# ordem
matriztexto.append("Trichoptera")
matriztexto.append(
    "Asa anterior sem cerdas ou apenas com cerdas microscópicas. Aparelho bucal com mandíbula bem desenvolvida. Antena mais curta do que o comprimento do corpo.")
matriztexto.append(
    "Asa anterior e posterior sem células. Abdômen peciolado. Protórax grande, separado do mesotórax (cupins, siriris, aleluias, térmitas).")
# ordem
matriztexto.append("Isoptera")
matriztexto.append(
    "Asas com pelo menos uma célula caso esteja ausente, então abdômen peciolado e protórax reduzido, unido ao mesotórax.")
matriztexto.append(
    "Asas anterior e posterior diferentes na forma e na venação a anterior cerca de 1,5 vezes mais comprida, com menos de 20 células. Abdômen geralmente peciolado. Protórax reduzido, unido ao mesotórax (abelhas, vespas, cabas, marimbondos).")
# ordem
matriztexto.append("Hymenoptera")
matriztexto.append(
    "Asa anterior e posterior aproximadamente do mesmo comprimento, semelhantes na forma e na venação. Asa anterior com mais de 20 células. Abdômen não peciolado. Protórax grande, separado do mesotórax.")
matriztexto.append(
    "Aparelho bucal prolongado, em forma de rostro, com mandíbulas no ápice. Área costal da asa anterior geralmente com uma ou duas veias transversais, raramente mais. Pernas longas e finas.")
# ordem
matriztexto.append("Mecoptera")
matriztexto.append(
    "Aparelho bucal sem projeção em forma de rostro. Área costal da asa anterior geralmente com mais de duas veias transversais.")
matriztexto.append(
    "Base da asa posterior mais larga do que a da asa anterior. Veias terminam sem ramificação na margem da asa. Asa anterior geralmente medindo mais de 8 mm de comprimento.")
# ordem
matriztexto.append("Mecoptera")
matriztexto.append(
    "Base da asa posterior mais estreita que a da asa anterior ou, no máximo, da mesma largura. Veias quase sempre bifurcadas próximo à margem da asa (exceto em espécies diminutas de Coniopterygidae, que possuem asa anterior com menos de 5 mm de comprimento e cobertas de pó esbranquiçado) (formigas-leão).")
# ordem
matriztexto.append("Neuroptera")
matriztexto.append("Tarsos com quatro artículos ou menos.")
matriztexto.append(
    "Aparelho bucal mastigador mandíbulas movendo-se em plano transversal. Palpo maxilar e labial presentes.")
matriztexto.append(
    "Asa anterior e posterior com numerosas células e veias transversais.")
matriztexto.append(
    "Antena curta, diminuta, cerdiforme, com menos de seis artículos. Asas, quando em repouso, estendidas lateralmente ao tórax ou posteriormente sobre o abdômen, mas não de forma plana. Área anal da asa posterior reduzida. Cerco com um artículo (libélulas, jacintas, lava-bundas).")
# ordem
matriztexto.append("Odonata")
matriztexto.append(
    "Antena longa, conspícua, com mais de seis artículos. Asas, quando em repouso, estendidas sobre o abdômen de forma plana. Área anal da asa posterior dobrada em leque quando em repouso. Cerco geralmente com vários artículos.")
# ordem
matriztexto.append("Plecoptera")
matriztexto.append(
    "Asa anterior e posterior sem nenhuma ou com poucas células e veias transversais.")
matriztexto.append(
    "Abdômen geralmente peciolado. Pescoço estreito. Asa anterior com uma ou duas veias e asa posterior com uma ou nenhuma veia. Antena geniculada (dobrada em cotovelo) entre o escapo e o pedicelo escapo mais comprido que o pedicelo (Chalcidoidea).")
# ordem
matriztexto.append("Hymenoptera")
matriztexto.append(
    "Abdômen não peciolado. Pescoço largo. Asa anterior com duas veias ou mais, asa posterior geralmente com mais de uma veia. Antena não geniculada.")
matriztexto.append(
    "Tarsômero basal anterior maior que os demais, dilatado, transformado em glândula produtora de seda.")
# ordem
matriztexto.append("Embioptera")
matriztexto.append("Tarsômero basal da perna anterior subigual aos demais.")
matriztexto.append(
    "Tarsos tetrâmeros. Asa anterior é posterior subiguais no comprimento (cupins, siriris, aleluias, térmitas).")
# ordem
matriztexto.append("Isoptera")
matriztexto.append(
    "Tarsos dímeros ou trímeros. Asa posterior mais curta que a asa anterior.")
matriztexto.append(
    "Cerco ausente. Antena filiforme, com 1 3 artículos ou mais. Asa anterior com pelo menos quatro veias longitudinais (R, M, CuA, CuP e A).")
# ordem
matriztexto.append("Psocoptera")
matriztexto.append(
    "Cerco com um artículo. Antena submoniliforme, com nove artículos. Asa anterior com três veias longitudinais (R, M e CuA).")
# ordem
matriztexto.append("Zoraptera")
matriztexto.append(
    "Aparelho bucal sugador, em forma de rostro. Palpo maxilar e labial estão ausentes (afídeos, pulgões, cigarras, cigarrinhas, percevejos).")
matriztexto.append(
    "Aparelho bucal mastigador. Mandíbula com movimentos no plano horizontal.")
matriztexto.append(
    "Asa posterior mais larga que a anterior, com dobras longitudinais em forma de leque.")
matriztexto.append(
    "Pronoto com lobo lateral descendente bem desenvolvido. Perna posterior quase sempre modificada para o salto, com fêmur engrossado. Fêmur e tíbia posteriores mais longos do que os respectivos segmentos das pernas anterior e média. Se pernas posterior e média semelhantes, então corpo subcilíndrico e perna anterior fossorial. Muitos produzem sons (gafanhotos, grilos, esperanças, paquinhas).")
# ordem
matriztexto.append("Orthoptera")
matriztexto.append(
    "Pronoto sem lobo lateral descendente bem desenvolvido. Perna posterior não modificada para o salto. Se maior que a perna média, então o fêmur não é engrossado. Se perna anterior fossorial, então corpo ovalado e achatado dorsoventralmente. Incapazes de produzir sons ou produzindo somente chiados.")
matriztexto.append(
    "Corpo largo, achatado dorso-ventralmente. Cabeça quase ou totalmente oculta pelo pronoto em vista dorsal. Pernas curtas e fortes, subiguais na forma e no tamanho, com as tíbias espinhosas (baratas).")
# ordem
matriztexto.append("Blattaria")
matriztexto.append(
    "Corpo geralmente estreito, alongado. Cabeça exposta. Pernas delgadas, anteriores geralmente mais longas, às vezes raptoriais. Tíbias sem espinhos.")
matriztexto.append(
    "Perna anterior raptorial. Protórax geralmente mais longo que o mesotórax. Cerco com vários articulas (louva-a-deus, põe-mesa).")
# ordem
matriztexto.append("Mantodea")
matriztexto.append(
    "Asa posterior um tanto semelhante à anterior, sem dobras longitudinais. Asa anterior com base esclerosada separada do restante por uma linha de fraqueza, que permite a quebra da asa (cupins, siriris, aleluias, térmitas).")
# ordem
matriztexto.append("Isoptera")
matriztexto.append(
    "Perna anterior não raptorial. Protórax mais curto do que o mesotórax. Cerco com um articulo (bichos-paus, bichos-graveto).")
# ordem
matriztexto.append("Phasmatodea")
matriztexto.append(
    "Aparelho bucal sugador, em forma de rostro (tubo adaptado para sugar), geralmente alongado, surgindo da parte ventral da cabeça e geralmente dirigido para trás. Palpo maxilar e labial ausentes (pulgões, cochonilhas, cigarras, cigarrinhas, percevejos, baratas d'água) - Ordem Hemiptera - ir até subordem.")
matriztexto.append(
    "Rostro originando-se na região anterior da cabeça, com três ou quatro artículos quando três, nunca ultrapassando o primeiro par de coxas. Antena com quatro ou cinco artículos, nunca cerdiforme. Asa anterior geralmente com a metade basal coriácea e a metade distai membranosa (hemiélitro), plana sobre o abdômen, a parte membranosa sobrepondo-se quando em repouso (percevejos).")
# ordem
matriztexto.append("Heteroptera")
matriztexto.append(
    "Rostro originando-se na região posterior da cabeça ou aparentemente entre as coxas anteriores, sempre com três artículos. Antena cerdiforme ou com mais de cinco articulas. Asa anterior de textura uniforme, pergaminácea (tégmina), às vezes membranosa, geralmente tectiforme.")
matriztexto.append(
    "Tarsos trímeros. Flagelo geralmente curto, cerdiforme. Rostro saindo da parte posterior da cabeça. Venação geralmente bem desenvolvida. Insetos de vida livre (cigarras, cigarrinhas).")
# ordem
matriztexto.append("Auchenorryncha")
matriztexto.append(
    "Tarsos mono ou dímeros. Flagelo geralmente longo, filiforme, com articulação distinta, nunca com menos de seis articulas. Rostro, quando presente, saindo entre as coxas anteriores. Venação reduzida. Insetos geralmente fixos ao substrato (pulgões, cochonilhas, psilídeos).")
# ordem
matriztexto.append("Sternorrhyncha")
matriztexto.append("Asas ausentes, vestigiais ou rudimentares")
matriztexto.append(
    "Sem aparência de inseto adulto. Tórax sem pernas ou com um a três pares reduzidos.")
matriztexto.append(
    "Corpo geralmente escamiforme, coberto com cera. Aparelho bucal sugador, com rostro surgindo da parte posterior da região ventral da cabeça. Insetos sésseis sob o substrato (cochonilhas).")
# ordem
matriztexto.append("Sternorrhyncha")
matriztexto.append(
    "Corpo vermiforme, sem segmentação distinta. Endoparasita de outros insetos, principalmente Hymenoptera e Hemiptera. Cabeça fundida ao tórax (cefalotórax), achatada dorsoventralmente, protraída entre segmentos abdominais do hospedeiro (fêmea larviforme de estrepsípteros).")
# ordem
matriztexto.append("Strepsiptera")
matriztexto.append(
    "Com aparência de inseto adulto, ou pelo menos de ninfa. Tórax com dois ou três pares de pernas, geralmente articuladas e com garras apicais que podem ser cônicas ou reduzidas.")
matriztexto.append(
    "Antena ausente. Perna anterior desenvolvida, projetada para frente, com função sensorial. Menos de 1,5 mm de comprimento.")
# ordem
matriztexto.append("Protura")
matriztexto.append(
    "Antena presente, às vezes muito reduzida. Perna anterior geralmente cursorial, às vezes fossorial, raptorial ou reduzida.")
matriztexto.append(
    "Abdômen com seis segmentos, com um colóforo no esternito I e geralmente com uma pequena furca (ou fúrcula) no esternito IV, bifurcada, para o salto. Geralmente com menos de 6 mm de comprimento.")
# ordem
matriztexto.append("Collembola")
matriztexto.append("Abdômen com mais de seis segmentos, sem colóforo e furca.")
matriztexto.append(
    "Abdômen com pares de estilos ventrais em dois ou mais segmentos. Ápice do abdômen com um par de fórceps ou com dois ou três apêndices articulados.")
matriztexto.append(
    "Ápice do abdômen com cercos, que podem ser multiarticulados ou em forma de pinça. Estilos abdominais ventrais presentes nos segmentos I-VII ou H-VII. Tarsos monômeros. Olhos compostos ausentes. Corpo sem escamas.")
# ordem
matriztexto.append("Diplura")
matriztexto.append(
    "Ápice do abdômen com três apêndices multiarticulados. Estilos ventrais abdominais presentes nos segmentos liIX, VII-IX ou VIII-IX. Tarsos di, tri ou tetrâmeros. Olhos compostos geralmente presentes. Corpo com escamas.")
matriztexto.append(
    "Corpo um tanto cilíndrico. Tórax distintamente arqueado. Olhos compostos grandes, geralmente contíguos. Paracerco (filamento caudal mediano) mais longo do que os cercos (traças saltadoras, silvestres).")
# ordem
matriztexto.append("Archaeognatha")
matriztexto.append(
    "Corpo achatado dorso-ventralmente. Tórax plano. Olhos compostos pequenos, distanciados entre si, ou ausentes. Paracerco subigual ao comprimento dos cercos (traças-de-livros).")
# ordem
matriztexto.append("Zygentoma")
matriztexto.append(
    "Abdômen sem estilos ventrais. Ápice do abdômen raramente com apêndices.")
matriztexto.append(
    "Corpo achatado lateral ou dorso-ventralmente. Ectoparasitas de aves, mamíferos ou abelhas, geralmente encontrados sobre o hospedeiro.")
matriztexto.append("Tarsos pentâmeros. Antena curta, geralmente encaixada em sulco.")
matriztexto.append(
    "Corpo achatado lateralmente. Pernas projetadas ventralmente, as posteriores mais desenvolvidas, adaptadas para o salto (pulgas).")
# ordem
matriztexto.append("Siphonaptera")
matriztexto.append(
    "Corpo achatado dorso-ventralmente. Pernas projetadas lateralmente, as posteriores subiguais às anteriores e médias no tamanho (moscas ectoparasitas: Braulidae, Hippoboscidae, Streblidae e Nycteribiidae).")
# ordem
matriztexto.append("Diptera")
matriztexto.append("Tarsos mono, di ou trímeros.")
matriztexto.append(
    "Tarsos trímeros. Antena mais comprida que a cabeça (percevejos).")
# ordem
matriztexto.append("Heteroptera")
matriztexto.append(
    "Tarsos monômeros. Antena mais curta que a cabeça (piolhos mastigadores, piolhos sugadores, chato).")
# ordem
matriztexto.append("Phthiraptera")
matriztexto.append("Corpo geralmente não achatado e de vida livre.")
matriztexto.append(
    "Olho composto ausente. Pteroteca ausente. Rastro surgindo da parte posterior da região ventral da cabeça. Palpo maxilar e labial ausentes. Insetos fitófagos. (cochonilhas: Coccoidea).")
# ordem
matriztexto.append("Sternorrhyncha")
matriztexto.append(
    "Olhos compostos presentes (às vezes reduzido ou ausente). Pteroteca geralmente presente. Tarsos com dois a cinco articulas (monômeros em alguns Ephemeroptera, Thysanoptera e Hemiptera).")
matriztexto.append(
    "Abdômen geralmente peciolado. Se diferente, então antena geniculada, escapo muito mais longo que o pedicelo (formigas e vespas).")
# ordem
matriztexto.append("Hymenoptera")
matriztexto.append("Abdômen livre ou séssil. Antena nunca geniculada.")
matriztexto.append(
    "Mesotórax muito desenvolvido pró- e metatórax reduzidos. Halter geralmente presente se ausente, então cabeça muito móvel, com pescoço estreito. Tarsos pentâmeros. Antena mais curta que a largura da cabeça, geralmente com três artículos, com arista apical (dípteros ápteros).")
# ordem
matriztexto.append("Diptera")
matriztexto.append(
    "Pró- e metatórax geralmente distintos se reduzidos, então pescoço largo ou ausente. Halter ausente. Tarsos mono ou dímeros. Antena mais longa que a largura da cabeça.")
matriztexto.append(
    "Corpo coberto com escamas e cerdas. Espirotromba com palpo maxilar reduzido ou inconspícuo. Antena longa e multiarticulada (mariposas ápteras).")
# ordem
matriztexto.append("Lepidoptera")
matriztexto.append(
    "Corpo sem escamas e, se cerdoso, com poucas cerdas. Aparelho bucal variável, nunca em forma de espirotromba, às vezes in conspícuo. Antena com forma variável.")
matriztexto.append("Aparelho bucal sugador, adaptado para picar e sugar.")
matriztexto.append(
    "Tarso com arólio em forma de lâmina eversível, com ou sem garras. Aparelho bucal cônico, sem articulação. Palpo maxilar e labial presentes (tripes, lacerdinhas).")
# ordem
matriztexto.append("Thysanoptera")
matriztexto.append(
    "Tarso sem arólio eversível, com duas garras (raramente uma). Aparelho bucal triangular ou alongado, geralmente articulado, raramente ausente. Palpo maxilar e labial ausentes (afídeos).")
# ordem
matriztexto.append("Sternorrhyncha")
matriztexto.append("Aparelho bucal mastigador, com mandíbulas opostas.")
matriztexto.append(
    "Cabeça com a área abaixo da antena (pós-clípeo) geralmente intumescida, bem desenvolvida. Protórax inconspícuo, menor que mesotórax ou metatórax. Tarsos di ou trímeros. Cerco ausente.")
# ordem
matriztexto.append("Psocoptera")
matriztexto.append(
    "Cabeça sem área intumescida abaixo da antena. Protórax conspícuo, aproximadamente igual ou maior que o mesotórax (exceto em Phasmatodea). Tarsos variáveis. Cerco variável.")
matriztexto.append(
    "Tarsos dímeros, tarsômero basal menor. Cerco simples. Antena submoniliforme, com oito ou nove articulas. Menos de 4 mm de comprimento.")
# ordem
matriztexto.append("Zoraptera")
matriztexto.append(
    "Tarsos com três a cinco artículos (tarso posterior raramente dímero). Cerco ausente ou com dois ou mais artículos se simples, então corpo com mais de 10 mm de comprimento. Antena variável.")
matriztexto.append(
    "Tarsômero basal da perna anterior intumescido, transformado em glândula produtora de seda.")
# ordem
matriztexto.append("Embioptera")
matriztexto.append("Tarsômero basal anterior subigual aos demais.")
matriztexto.append(
    "Pronoto com lobo lateral descendente bem desenvolvido. Perna posterior quase sempre modificada para o salto, com fêmur engrossado e fêmur e tíbia mais longos que os respectivos segmentos das pernas anterior e média (quando perna posterior e média semelhantes, então perna anterior fossorial). Vários grupos produzem sons (gafanhotos, grilos, esperanças, paquinhas).")
# ordem
matriztexto.append("Orthoptera")
matriztexto.append(
    "Pronoto sem lobo lateral descendente desenvolvido. Perna posterior não modificada para o salto se um tanto maior que a perna média, então fêmur não engrossado. Se perna anterior fossorial, então corpo ovalado e achatado. Incapazes de produzir sons ou produzem somente chiados.")
matriztexto.append(
    "Perna anterior raptorial. Protórax geralmente muito mais comprido que o mesotórax (louva-a-deus).")
# ordem
matriztexto.append("Mantodea")
matriztexto.append(
    "Perna anterior não raptorial. Protórax não alongado se alongado, mais curto que o mesotórax.")
matriztexto.append(
    "Peças bucais protraídas. Cápsula cefálica fechada ventralmente, formando uma área gular entre a base do lábio e a margem posterior da cabeça. Antena com 1 1 artículos ou menos. Palpo maxilar com quatro artículos ou menos. Clípeo inconspícuo (besouros sem ou com élitros muito curtos).")
# ordem
matriztexto.append("Coleoptera")
matriztexto.append(
    "Peças bucais retraídas. Cápsula cefálica aberta ventralmente, assim o lábio atinge a margem posterior da cabeça. Antena geralmente com 12 artículos ou mais se menos, então clípeo distinto. Palpo maxilar com cinco artículos.")
matriztexto.append("Cerco com quatro artículos ou mais.")
matriztexto.append(
    "Cabeça hipognata ou opistognata. Antena longa, filiforme. Pronoto em forma de escudo e um tanto arredondado, geralmente cobrindo total ou parcialmente a cabeça em vista dorsal. Corpo achatado dorso-ventralmente (baratas).")
# ordem
matriztexto.append("Blattaria")
matriztexto.append(
    "Cabeça prognata. Antena moniliforme. Pronoto diferente cabeça exposta. Corpo cilíndrico (cupins, siriris, aleluias, térmitas).")
# ordem
matriztexto.append("Isoptera")
matriztexto.append("Cerco com um a três artículos.")
matriztexto.append(
    "Protórax mais curto que o mesotórax. Tarsos pentâmeros. Corpo alongado e estreito, em forma de graveto. Geralmente mais de 30 mm de comprimento (bichos-paus, bichos-gravetos, mané-magro).")
# ordem
matriztexto.append("Phasmatodea")
matriztexto.append(
    "Protórax tão longo quanto comprimento do mesotórax ou mais longo. Tarsos com dois a quatro tarsômeros. Corpo sem forma de graveto. Geralmente menos de 30 mm de comprimento se maiores, então cerco grande, em forma de pinça.")
matriztexto.append(
    "Coxas relativamente grandes, aproximadas entre si. Cerco muito pequeno, com um a três artículos, divergentes. Tarsos tetrâmeros. Corpo geralmente pálido ou branco (cupins, térmitas).")
# ordem
matriztexto.append("Isoptera")
matriztexto.append(
    "Coxas pequenas, distanciadas entre si. Cerco grande, convergente, em forma de pinça. Tarsos trímeros, raramente dímeros. Corpo geralmente marrom-escuro a preto (tesourinhas, lacrainhas).")
# ordem
matriztexto.append("Dermaptera")


@dataclass
class MatrizOrdemHexapoda:
    matrizij: str
    matrizik: str
    indiceij: int
    indiceik: int
    i: int
    j: int
    k: int
    indiceij: int
    indiceik: int
    matrizindice: list
    matriztexto: list

    def __init__(self):
        self.matrizindice = matrizindice
        self.matriztexto = matriztexto
        self.i = 0
        self.j = 0
        self.k = 1
        self.indiceij = matrizindice.index("[" + str(self.i) + "][" + str(self.j) + "]")
        self.indiceik = matrizindice.index("[" + str(self.i) + "][" + str(self.k) + "]")
        if self.indiceij >= 0:
            self.matrizij = matriztexto[self.indiceij]
        else:
            self.matrizij = ""
        if self.indiceik >= 0:
            self.matrizik = matriztexto[self.indiceik]
        else:
            self.matrizik = ""


def __update_text(MatrizOrdemHexapoda):
    MatrizOrdemHexapoda.indiceij = matrizindice.index("[" + str(MatrizOrdemHexapoda.i) + "][" + str(MatrizOrdemHexapoda.j) + "]")
    MatrizOrdemHexapoda.indiceik = matrizindice.index("[" + str(MatrizOrdemHexapoda.i) + "][" + str(MatrizOrdemHexapoda.k) + "]")
    if MatrizOrdemHexapoda.indiceij >= 0:
        MatrizOrdemHexapoda.matrizij = matriztexto[MatrizOrdemHexapoda.indiceij]
    else:
        MatrizOrdemHexapoda.matrizij = ""
    if MatrizOrdemHexapoda.indiceik >= 0:
        MatrizOrdemHexapoda.matrizik = matriztexto[MatrizOrdemHexapoda.indiceik]
    else:
        MatrizOrdemHexapoda.matrizik = ""
