from mission8 import *

ctextin = "OUEVEBEKCOAAFEOITIBEHIAKUTNOTQDRHKRITEIHAEGOJARSHNTTEESTAOMOSEODUEDTWMGTCWOCCWDETFAEIEHIOICIATCHFLNNOKNIATVIOUADTUAATTROAHWNFASHLDIIESETTTLROMWTFIEAOYALARMYAHUHAKKWINLDTENNKYLDTABWWNOIONIRISHBAHOGNMNUKLKEEGTSEIEATRHIGLTENSDARFHAILWNIEWDBIBNRATUNFANTCYRHEAERASTMTHUCASEVGSIMOSIEETEDMEORGDONESBPTMETREUAAVTCWATNEDTENOUTTTEFETEHEEWATMTHRTBEHAAYSABANTWORDABSALSNYPIIBNASYWLEKSDTATTOEEOSHTSHETLLEAWATWHEOOVIFDBNOTUSOAEWHLEUVNETEAAODMRUDYHNREHNVRETATGHDAHTHEEORSONOREUEBEPIIDTNZSHSLEERPHNCDLOHOGOHUOTATAVTGFWDDATUIDENNEHHIATTCRIHNOEDWODVTLDNNDSBAIAIEIOILNTEMIRYTTEYTSTHIRKWCUTLBHSEBADNTAERTIEAEAEWDACNAKSEUTEBAABAETTSTDMHTTARFYNYHNEFHSGEYUSSOSLNINEIADARAWWHIADODKTRZCUANITIEUHAETSNOTAIONOTADLRROEFIFDAMOTHETAONRUIALTYEDLHUXTELLNTTWTWSGVBEHOTIAIEOAFAOEAEOFNSCHNLEBNFSDTTENFHGOORAEEMTDTECOVNDTKXTOAIFOAUREDOMNSEIITSUIRPBIEDAYTCHHLNRUANNWBHTITKOEUOTWGWTRHDSTSQIMEAHASEELKRISUNIIITAATDHSHINHERWHONPLEKTDAERODIEPDAFETLETPIRGIICCGYTEEAENRINNHTICISCSRNANNHEALLTCHIEOFDILEMOYEKEHDRSIBNILSETATDPEWNDRVHFAEEERNLHERNEIYTTDTDYSOIEUETOAUAFIAHIDDHGNTYNNTNTGEFILOTTWOTEPHNLWIVERWKHARTGEDTHENEOONADBHOUOTEEETNEHKLRNOADNNHITBAEOTEGTNTMGTIHKAEEICNIDOMXEILOOEETDLTPYAPDSHDFNEATARFCITBRUETSEEIDUINHBELTLGALFCMIATAOOEIDTSGKDHEHTCEDTISAHIIPJBEOOAWOUIUONNNWWTCUTSUROAMTKOOOHTIHHLRMBDIEDYUOEAAMOSYNESDLIHITTETRTEGTEAESBLHELSKSNSIJOLNAAWSSTEGSTUSEADMGATINIEESPBTMHOTIWADDTEASTAATHLAHLGSETNALEPDADNISULENUGWVAWTDNORLIOCCHNENAOTISICSIMTEHADGKAFMIONAERINTGTESOTHOOIIRHA"

split_list = split_string_every_n_blocks(ctextin, 41)

for i in range(len(split_list)):
    split_list[i] = f"{ic(split_list[i])}\n"
    
print (thing for thing in split_list)