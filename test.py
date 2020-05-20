from progress.bar import Bar
import time

bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
    time.sleep(0.1)
# bar.finish()