#include "SineOscTestModule.h"

	SineOscTestModule::SineOscTestModule(AudioModuleId id , SineOscTestModuleParams*p):
	AudioModule(id,p),_phase(0.f){
		
	}

	void SineOscTestModule::process(ProcessData &data){

		const float k = 2.* 3.14159265358979323846;

		const float t = _params->_f /data._framerate* k;
		for(int i=0;i<data._nframes;i++)
		{
			_phase += t;

			for(int j=0;j<data._nOutputBuffers;j++)
				data._outputbuffers[j][i] = sinf(_phase);
		}
		
		int n=_phase / k;
		_phase-=k*n;
	}