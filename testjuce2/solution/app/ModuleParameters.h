#pragma once
#include <vector>
#include <string>
//comment assurer la thread safety ? ?
//pattern concurrent serait bien ..
class ModuleParameters{
public :
	//un concurrent queue mp sc
	typedef int ParameterId;
	typedef int ModuleParameterId;
	typedef float ParameterValue; // pourrait etre any
	class Listener{
	public:
		virtual void moduleParametersChanged()=0;
	};
	void addListener(Listener *l){
		_listeners.push_back(l);
	}
	ModuleParameters(ModuleParameterId mpi):_mpi(mpi){}
	void setParameter(ParameterId pi, ParameterValue val){
		internalSetParameter(pi, val);
		notifyListeners();
	}
	void notifyListeners(){
		for(std::vector<Listener*>::iterator i=_listeners.begin();i!=_listeners.end();i++)
			(*i)->moduleParametersChanged();
	}
private:
	virtual void internalSetParameter(ParameterId pi, ParameterValue val){}
	std::vector<Listener*> _listeners;
	ModuleParameterId _mpi;
};