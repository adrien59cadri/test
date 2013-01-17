#pragma once

#include "IControlCenter.h"

class Editor : public Component {
public:
	Editor(IControlCenter & icc);
	virtual void paint(Graphics & inG);
private:
	IControlCenter & _icc;
};