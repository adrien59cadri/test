#include "IOEngine.h"
#include "SineOscTestModule.h"

IOEngine::IOEngine():_framerate(0.f){
	SineOscTestModuleParams * p= new SineOscTestModuleParams(0,440.f);
	SineOscTestModule*m = new SineOscTestModule(0,p);
	_pparams = p;
	_pmodule = m;
}

IOEngine::~IOEngine(){
	delete _pmodule;
	delete _pparams;
}

void IOEngine::audioDeviceIOCallback (const float** inputChannelData,
                                        int numInputChannels,
                                        float** outputChannelData,
                                        int numOutputChannels,
                                        int numSamples) {

											ProcessData data;
											data._framerate = _framerate;
											data._inputbuffers = inputChannelData;
											data._outputbuffers = outputChannelData;
											data._nframes = numSamples;
											data._nOutputBuffers = numOutputChannels;
											data._nInputBuffers = numInputChannels;
											_pmodule->process(data);

}
void IOEngine::audioDeviceAboutToStart (AudioIODevice* device) {
	set_framerate( device->getCurrentSampleRate());
}
    /** Called to indicate that the device has stopped. */
void IOEngine::audioDeviceStopped(){

}
