#pragma once
#include "juce.h"

class IControlCenter{
public:
	virtual AudioDeviceManager & getAudioDeviceManager()=0;
private:
	AudioDeviceManager _adm;
};