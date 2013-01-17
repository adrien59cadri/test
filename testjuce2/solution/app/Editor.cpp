
#include "Editor.h"
Editor::Editor(IControlCenter & icc):_icc(icc){
	
}

void Editor::paint(Graphics & inG){
	inG.fillAll(Colours::blue);
}
