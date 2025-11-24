import jpype
from jpype import JClass
from config import jvm_path,jar_path


#Zemberek kütüphanesinin entegre edeilmesi ve JVM£nin başlatılması
if not jpype.isJVMStarted():
    jpype.startJVM(
        jvm_path,
        f"-Djava.class.path={jar_path}",
        "-ea"
    )

TurkishMorphology = jpype.JClass("zemberek.morphology.TurkishMorphology")
TurkishSpellChecker=JClass("zemberek.normalization.TurkishSpellChecker")
morphology = TurkishMorphology.createWithDefaults()
spell_checker = TurkishSpellChecker(morphology)


