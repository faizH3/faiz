total_umur_dalam_hari = 75
jumlah_hari_dalam_sebulan = 30

bulan = total_umur_dalam_hari/jumlah_hari_dalam_sebulan
hari = total_umur_dalam_hari % jumlah_hari_dalam_sebulan

print('umur bayi sekarang {} bulan dan {} hari'.format(bulan,hari))
print('umur bayi sekarang {1} bulan dan {0} hari'.format(hari,bulan))
print('umur bayi sekarang %s bulan dan %s hari'%(bulan,hari))
print('umur bayi sekarang',bulan,'bulan dan',hari,'hari')
print('umur bayi sekarang '+str(bulan)+' bulan dan '+str(hari)+' hari')