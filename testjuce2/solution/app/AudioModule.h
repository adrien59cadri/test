#pragma once
#include "ModuleParameters.h"

#include "ProcessData.h"
class IAudioModule{
public:
	virtual void process(ProcessData &data)=0;
	
	typedef int AudioModuleId;
};


template <typename TParam>
class AudioModule:
	public IAudioModule,
	public ModuleParameters::Listener
{
public:
	AudioModule(AudioModuleId id, TParam * p)
		:_params(p),_id(id){
		_params->addListener(this);
	}
	virtual void moduleParametersChanged(){}
	TParam *getParameters(){return _params;}
	virtual void process(ProcessData &data){}

protected:
	TParam *_params;
	AudioModuleId _id;//l id pourrait etre un id unique ou une ip dans un graph
	//pour l instant on s en fout
};