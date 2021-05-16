#!/bin/bash

# =====================================
# install ViniAudit into a virtual env
# =====================================

# VERSION: 0.1.0
# =====================================
export DEBIAN_FRONTEND=noninteractive

WORKDIR=/root
TMPDIR=/tmp

# =====================================
# install ViniAudit
# =====================================
cd ${WORKDIR}
virtualenv -p python3 ViniAudit
source ${WORKDIR}/ViniAudit/bin/activate
pip install ViniAudit

echo -e "\n\nViniAudit Installation Complete!\n\n"
