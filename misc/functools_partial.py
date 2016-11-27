def write_result(res, log=None):
	if log is not None:
		log.info("Got: %r", res)

def add(x, y):
	return x + y

if __name__ == '__main__':
	import logging
	from multiprocessing import Pool
	from functools import partial
	
	logging.basicConfig(level=logging.INFO)
	log = logging.getLogger('test')

	p = Pool()
	p.apply_async(add, (3, 4), callback=partial(write_result, log=log))
	p.close()
	p.join()
	
