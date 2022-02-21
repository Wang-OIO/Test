from odps.udf import annotate
from
@annotate('bigint,bigint->bigint')
class NumAdd(object):
   def evaluate(self, arg0, arg1):
       if None in (arg0, arg1):
           return None
       return arg0 + arg1