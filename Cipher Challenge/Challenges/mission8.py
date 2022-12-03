def split_by_index(ctext: str, n: int) -> int:
    ctext = ctext.replace(" ", "")
    ctext.upper()

    return ctext[::n] 
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
def remove_consecutive_indexes(input: str, start: int, end: int) -> str:
        cipher_text_list = list(input)
        for i in range((end - start) + 1):
            del cipher_text_list[start - 1::start]

        finallist = ''.join(cipher_text_list)
        return finallist
def split_string_every_n_blocks(input_string: str, blocklength: int) -> list:
    blocklength = int(blocklength)
    ciphertext = input_string
    list_out = []
    rangeofexecution = len(input_string) / blocklength
    rangeofexecution = int(rangeofexecution)
    
    for i in range(rangeofexecution):
        new_block = ciphertext[:blocklength]
        list_out.append(new_block)
        ciphertext = ciphertext.replace(new_block, '', 1)
        
    return list_out    


ctextin = "OUEVE BEKCO AAFEO ITIBE HIAKU TNOTQ DRHKR ITEIH AEGOJ ARSHN TTEES TAOMO SEODU EDTWM GTCWO CCWDE TFAEI EHIOI CIATC HFLNN OKNIA TVIOU ADTUA ATTRO AHWNF ASHLD IIESE TTTLR OMWTF IEAOY ALARM YAHUH AKKWI NLDTE NNKYL DTABW WNOIO NIRIS HBAHO GNMNU KLKEE GTSEI EATRH IGLTE NSDAR FHAIL WNIEW DBIBN RATUN FANTC YRHEA ERAST MTHUC ASEVG SIMOS IEETE DMEOR GDONE SBPTM ETREU AAVTC WATNE DTENO UTTTE FETEH EEWAT MTHRT BEHAA YSABA NTWOR DABSA LSNYP IIBNA SYWLE KSDTA TTOEE OSHTS HETLL EAWAT WHEOO VIFDB NOTUS OAEWH LEUVN ETEAA ODMRU DYHNR EHNVR ETATG HDAHT HEEOR SONOR EUEBE PIIDT NZSHS LEERP HNCDL OHOGO HUOTA TAVTG FWDDA TUIDE NNEHH IATTC RIHNO EDWOD VTLDN NDSBA IAIEI OILNT EMIRY TTEYT STHIR KWCUT LBHSE BADNT AERTI EAEAE WDACN AKSEU TEBAA BAETT STDMH TTARF YNYHN EFHSG EYUSS OSLNI NEIAD ARAWW HIADO DKTRZ CUANI TIEUH AETSN OTAIO NOTAD LRROE FIFDA MOTHE TAONR UIALT YEDLH UXTEL LNTTW TWSGV BEHOT IAIEO AFAOE AEOFN SCHNL EBNFS DTTEN FHGOO RAEEM TDTEC OVNDT KXTOA IFOAU REDOM NSEII TSUIR PBIED AYTCH HLNRU ANNWB HTITK OEUOT WGWTR HDSTS QIMEA HASEE LKRIS UNIII TAATD HSHIN HERWH ONPLE KTDAE RODIE PDAFE TLETP IRGII CCGYT EEAEN RINNH TICIS CSRNA NNHEA LLTCH IEOFD ILEMO YEKEH DRSIB NILSE TATDP EWNDR VHFAE EERNL HERNE IYTTD TDYSO IEUET OAUAF IAHID DHGNT YNNTN TGEFI LOTTW OTEPH NLWIV ERWKH ARTGE DTHEN EOONA DBHOU OTEEE TNEHK LRNOA DNNHI TBAEO TEGTN TMGTI HKAEE ICNID OMXEI LOOEE TDLTP YAPDS HDFNE ATARF CITBR UETSE EIDUI NHBEL TLGAL FCMIA TAOOE IDTSG KDHEH TCEDT ISAHI IPJBE OOAWO UIUON NNWWT CUTSU ROAMT KOOOH TIHHL RMBDI EDYUO EAAMO SYNES DLIHI TTETR TEGTE AESBL HELSK SNSIJ OLNAA WSSTE GSTUS EADMG ATINI EESPB TMHOT IWADD TEAST AATHL AHLGS ETNAL EPDAD NISUL ENUGW VAWTD NORLI OCCHN ENAOT ISICS IMTEH ADGKA FMION AERIN TGTES OTHOO IIRHA"
ctextin = ctextin.replace(' ', '')

banana = split_string_every_n_blocks(ctextin, 1)
banana = ''.join(banana)

print(banana == ctextin)


