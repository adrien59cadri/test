#pragma once
#include "IControlCenter.h"
#include "IOEngine.h"
class ControlCenter:public IControlCenter,
	public ChangeListener{
public:
    virtual void changeListenerCallback (ChangeBroadcaster* source);

	ControlCenter();
	virtual AudioDeviceManager & getAudioDeviceManager();
	private:
	IOEngine _ioe;
	AudioDeviceManager _adm;
};