from re import S
import sys

from pyscsi.pyscsi import scsi_enum_inquiry as INQUIRY
from pyscsi.pyscsi.scsi import SCSI
from pyscsi.pyscsi.scsi_sense import SCSICheckCondition
from pyscsi.utils import init_device


def standart_read10():
  device = init_device('/dev/sdb')

  s = SCSI(device, 512)

  data = s.read10(0, 1)

  print(data.datain)

if __name__ == "__main__":
  standart_read10()
  