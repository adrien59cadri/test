#pragma once

#include "IControlCenter.h"

class Content : public TabbedComponent {
public:
	Content(IControlCenter & icc);
private:
	IControlCenter&_icc;
};