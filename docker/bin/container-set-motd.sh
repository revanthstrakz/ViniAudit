#!/bin/bash
cat <<'EOF' >> /root/.bashrc
cd ${HOME}
source ${HOME}/ViniAudit/bin/activate
echo -e "Welcome to ViniAudit!\nTo run ViniAudit, just type \`Vini -h\` to see the help documentation.\nHave fun!\n\n"
EOF