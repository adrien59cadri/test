#include "AudioModule.h"
#define _USE_MATH_DEFINES
#include <cmath>

	class SineOscTestModuleParams: public ModuleParameters{
	public:
		SineOscTestModuleParams(ModuleParameterId id, float freq):ModuleParameters(id), _f(freq){
		}
		float _f;
	};

class SineOscTestModule : public AudioModule<SineOscTestModuleParams>{
public:
	
	virtual void moduleParametersChanged(){}
	
	SineOscTestModule(AudioModuleId id, SineOscTestModuleParams*p);
	virtual void process(ProcessData &data);
private:
	float _phase;

};