pronouns = ['Ben','Sen','O','Biz','Siz','Onlar']
consonants = {
    'yumuşak': {'b','c','d','g','ğ','j','l','m','n','r','v','y','z'},
    'sert': {'ç','f','h','k','p','s','ş','t'}
}
vowels = ['a','e','i','ı','o','ö','u','ü']
endings = ['tim','tin','ti','tik','tiniz','ti']
verb_marker = ['mek','mak']

class TurkishVerb:
    def __init__ (self,verb_in):
        self.verb_in = verb_in
        verb_stem = verb_in[:-3]

        for p in pronouns:
            if verb_stem[-1] in consonants['sert']:
                endings = endings[pronouns.index(p)]
            else:
                endings = endings[pronouns.index(p)].replace('t','d')
            
        for p in pronouns:
            if verb_stem[-2:].find('u')!= -1 :
                verb_conjugation = verb_stem + endings[pronouns.index(p)].replace('i','u')
            elif verb_stem[-2:].find('o')!= -1 :
                verb_conjugation = verb_stem + endings[pronouns.index(p)].replace('i','u')
            elif verb_stem[-2:].find('a')!= -1 :
                verb_conjugation = verb_stem + endings[pronouns.index(p)].replace('i','ı')
            elif verb_stem[-2:].find('ı')!= -1 :
                verb_conjugation = verb_stem + endings[pronouns.index(p)].replace('i','ı')
            else:
                verb_conjugation = verb_stem + endings[pronouns.index(p)]
            print (p + ' ' + verb_conjugation)

            
verb_in = input('Please enter a Turkish verb: ')
conj = TurkishVerb(verb_in)

    