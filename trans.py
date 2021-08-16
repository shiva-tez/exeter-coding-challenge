from googletrans import Translator
import time
import os
 

startTime = time.time()

translater = Translator()

out = translater.translate("farewell", dest="fr")
print(out.text)
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
stats = os.stat('F:\Translate')
print(stats.st_size)

