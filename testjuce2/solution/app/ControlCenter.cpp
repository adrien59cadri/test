#include "ControlCenter.h"
#include "AudioModule.h"
	ControlCenter::ControlCenter(){
		AudioIODeviceCallback *callback=&_ioe;
		_adm.addAudioCallback(callback);
		_adm.addChangeListener(this);
	}
	AudioDeviceManager & ControlCenter::getAudioDeviceManager()
	{return _adm;}
	
void ControlCenter:: changeListenerCallback (ChangeBroadcaster* source){

	if(source!=&_adm)
		return;
	AudioDeviceManager::AudioDeviceSetup setup;
	_adm.getAudioDeviceSetup(setup);
	_ioe.set_framerate(setup.sampleRate);
	//more ?
}