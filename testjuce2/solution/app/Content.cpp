
#include "Editor.h"
#include "Content.h"

Content::Content(IControlCenter&icc):
TabbedComponent(TabbedButtonBar::TabsAtTop),
_icc(icc)
{
		addTab("settings",Colours::white,new AudioDeviceSelectorComponent(
			_icc.getAudioDeviceManager(),0,0,2,2,true,false,true,true)
			,true,0);
		addTab("editor",Colours::white,new Editor(_icc),true,1);

	}
