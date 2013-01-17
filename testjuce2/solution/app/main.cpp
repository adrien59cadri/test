#include "main.h"

MyAppW::MyAppW(MyJUCEApp*app):DialogWindow("application",Colours::white,false)
			,_app(app),_content(app->getCC()){
			setContentComponent(&_content);
			setUsingNativeTitleBar(true);
			setSize(800,600);
		}
START_JUCE_APPLICATION (MyJUCEApp)
  