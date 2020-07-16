import geni.portal as portal
import geni.rspec.pg as rspec

# Create request object to start building RSpec.
request = portal.context.makeRequestRSpec()

# Create a XenVM
node = request.XenVM("node")
node.disk_image = "urn:publicid:IDN+emulab.net+img+emulab-ops:UBUNTU18-64-STD"
node.routable_control_ip = "true"

node.addService(rspec.Execute(shell="/bin/sh",
                              command="sudo apt update"))
node.addService(rspec.Execute(shell="/bin/sh",
                              command="sudo apt install -y apache2"))
node.addService(rspec.Execute(shell="/bin/sh",
                              command='sudo suwf allow in "Apache Full"'))
node.addService(rspec.Execute(shell="/bin/sh",
                              command='sudo systemctl status apache2'))
# Print the RSpec enclosing page
portal.context.printRequestRSpec()

