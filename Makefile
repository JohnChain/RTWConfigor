UIPREFIX = TumConf
SRC = mainUI.py
all:
	pyuic5 $(UIPREFIX).ui -o $(UIPREFIX).py
	python $(SRC)
clean:
	rm -rf __pycache__