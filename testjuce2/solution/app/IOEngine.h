#pragma once

#include "juce.h"
#include "AudioModule.h"
//l engine permet de recevoir et envoyer de l audio
//il transmet cela au module audio principal

class IOEngine : public AudioIODeviceCallback{
public:
	IOEngine();
	virtual ~IOEngine();
	virtual void audioDeviceIOCallback (const float** inputChannelData,
                                        int numInputChannels,
                                        float** outputChannelData,
                                        int numOutputChannels,
                                        int numSamples) ;
    virtual void audioDeviceAboutToStart (AudioIODevice* device) ;

    /** Called to indicate that the device has stopped. */
    virtual void audioDeviceStopped() ;
	void set_framerate(float f){_framerate=f;}
private:
	IAudioModule* _pmodule;
	ModuleParameters * _pparams;
	float _framerate;
};