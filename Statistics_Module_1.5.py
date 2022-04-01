from tkinter import *

# Defining main window
window = Tk()
window.configure(background="#615F61")

# Defining frames
header = LabelFrame(window, borderwidth=0)
header.configure(background="#615F61")
header.grid(row=0, column=0, padx=7, pady=7)

root = LabelFrame(window)
root.config(background="#E7E4E7")
root.grid(row=1, column=0, padx=7, pady=7)

# Defining header
title = Label(header, text="Continuous Datatype Statistics Module", justify=CENTER, bg="#615F61")
title.config(font=("Arial Rounded MT Bold", 22))
title.pack()

# Defining functions
def compute():
	mean_A = Label(root, text="0", bg="#E7E4E7", width=11).grid(row=14, column=1)
	mean_dv_A = Label(root, text="N.A.", bg="#E7E4E7", width=11).grid(row=15, column=1)

	LL2 = float(row1_CIa.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*1) 
	LL3 = float(row1_CIa.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*2)
	LL4 = float(row1_CIa.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*3)
	LL5 = float(row1_CIa.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*4)
	LL6 = float(row1_CIa.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*5)
	LL7 = float(row1_CIa.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*6)
	LL8 = float(row1_CIa.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*7)
	LL9 = float(row1_CIa.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*8)
	LL10 = float(row1_CIa.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*9)
	row2_CIa = Label(root, bg="#E7E4E7", width=13, text=LL2)
	row3_CIa = Label(root, bg="#E7E4E7", width=13, text=LL3)
	row4_CIa = Label(root, bg="#E7E4E7", width=13, text=LL4)
	row5_CIa = Label(root, bg="#E7E4E7", width=13, text=LL5)
	row6_CIa = Label(root, bg="#E7E4E7", width=13, text=LL6)
	row7_CIa = Label(root, bg="#E7E4E7", width=13, text=LL7)
	row8_CIa = Label(root, bg="#E7E4E7", width=13, text=LL8)
	row9_CIa = Label(root, bg="#E7E4E7", width=13, text=LL9)
	row10_CIa = Label(root, bg="#E7E4E7", width=13, text=LL10)
	row2_CIa.grid(row=2, column=0)
	row3_CIa.grid(row=3, column=0)
	row4_CIa.grid(row=4, column=0)
	row5_CIa.grid(row=5, column=0)
	row6_CIa.grid(row=6, column=0)
	row7_CIa.grid(row=7, column=0)
	row8_CIa.grid(row=8, column=0)
	row9_CIa.grid(row=9, column=0)
	row10_CIa.grid(row=10, column=0)

	UL2 = float(row1_CIb.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*1) 
	UL3 = float(row1_CIb.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*2)
	UL4 = float(row1_CIb.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*3)
	UL5 = float(row1_CIb.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*4)
	UL6 = float(row1_CIb.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*5)
	UL7 = float(row1_CIb.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*6)
	UL8 = float(row1_CIb.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*7)
	UL9 = float(row1_CIb.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*8)
	UL10 = float(row1_CIb.get()) + ((float(row1_CIb.get()) - float(row1_CIa.get()))*9)
	row2_CIb = Label(root, bg="#E7E4E7", width=13, text=UL2)
	row3_CIb = Label(root, bg="#E7E4E7", width=13, text=UL3)
	row4_CIb = Label(root, bg="#E7E4E7", width=13, text=UL4)
	row5_CIb = Label(root, bg="#E7E4E7", width=13, text=UL5)
	row6_CIb = Label(root, bg="#E7E4E7", width=13, text=UL6)
	row7_CIb = Label(root, bg="#E7E4E7", width=13, text=UL7)
	row8_CIb = Label(root, bg="#E7E4E7", width=13, text=UL8)
	row9_CIb = Label(root, bg="#E7E4E7", width=13, text=UL9)
	row10_CIb = Label(root, bg="#E7E4E7", width=13, text=UL10)
	row2_CIb.grid(row=2, column=1)
	row3_CIb.grid(row=3, column=1)
	row4_CIb.grid(row=4, column=1)
	row5_CIb.grid(row=5, column=1)
	row6_CIb.grid(row=6, column=1)
	row7_CIb.grid(row=7, column=1)
	row8_CIb.grid(row=8, column=1)
	row9_CIb.grid(row=9, column=1)
	row10_CIb.grid(row=10, column=1)



	x1 = (float(row1_CIa.get())+float(row1_CIb.get()))/2
	if len(row1_fi.get())==0:
		f1 = 0
	else:
		f1 = int(row1_fi.get())
	fix1 = x1*f1
	row1_xi = Label(root, text=x1, width=10, bg="#E7E4E7", justify=CENTER).grid(row=1, column=2)
	row1_fixi = Label(root, text=fix1, width=10, bg="#E7E4E7", justify=CENTER).grid(row=1, column=4)

	x2 = (UL2+LL2)/2
	if len(row2_fi.get())==0:
		f2 = 0
	else:
		f2 = int(row2_fi.get())
	fix2 = x2*f2
	row2_xi = Label(root, text=x2, width=10, bg="#E7E4E7", justify=CENTER).grid(row=2, column=2)
	row2_fixi = Label(root, text=fix2, width=10, bg="#E7E4E7", justify=CENTER).grid(row=2, column=4)

	x3 = (UL3+LL3)/2
	if len(row3_fi.get())==0:
		f3 = 0
	else:
		f3 = int(row3_fi.get())
	fix1 = x1*f1
	fix3 = x3*f3
	row3_xi = Label(root, text=x3, width=10, bg="#E7E4E7", justify=CENTER).grid(row=3, column=2)
	row3_fixi = Label(root, text=fix3, width=10, bg="#E7E4E7", justify=CENTER).grid(row=3, column=4)

	x4 = (UL4+LL4)/2
	if len(row4_fi.get())==0:
		f4 = 0
	else:
		f4 = int(row4_fi.get())
	fix1 = x1*f1
	fix4 = x4*f4
	row4_xi = Label(root, text=x4, width=10, bg="#E7E4E7", justify=CENTER).grid(row=4, column=2)
	row4_fixi = Label(root, text=fix4, width=10, bg="#E7E4E7", justify=CENTER).grid(row=4, column=4)

	x5 = (UL5+LL5)/2
	if len(row5_fi.get())==0:
		f5 = 0
	else:
		f5 = int(row5_fi.get())
	fix5 = x5*f5
	row5_xi = Label(root, text=x5, width=10, bg="#E7E4E7", justify=CENTER).grid(row=5, column=2)
	row5_fixi = Label(root, text=fix5, width=10, bg="#E7E4E7", justify=CENTER).grid(row=5, column=4)

	x6 = (UL6+LL6)/2
	if len(row6_fi.get())==0:
		f6 =0
	else:
		f6 = int(row6_fi.get())
	fix6 = x6*f6
	row6_xi = Label(root, text=x6, width=10, bg="#E7E4E7", justify=CENTER).grid(row=6, column=2)
	row6_fixi = Label(root, text=fix6, width=10, bg="#E7E4E7", justify=CENTER).grid(row=6, column=4)

	x7 = (UL7+LL7)/2
	if len(row7_fi.get())==0:
		f7 = 0
	else:
		f7 = int(row7_fi.get())
	fix7 = x7*f7
	row7_xi = Label(root, text=x7, width=10, bg="#E7E4E7", justify=CENTER).grid(row=7, column=2)
	row7_fixi = Label(root, text=fix7, width=10, bg="#E7E4E7", justify=CENTER).grid(row=7, column=4)

	x8 = (UL8+LL8)/2
	if len(row8_fi.get())==0:
		f8 = 0
	else:
		f8 = int(row8_fi.get())
	fix8 = x8*f8
	row8_xi = Label(root, text=x8, width=10, bg="#E7E4E7", justify=CENTER).grid(row=8, column=2)
	row8_fixi = Label(root, text=fix8, width=10, bg="#E7E4E7", justify=CENTER).grid(row=8, column=4)

	x9 = (UL9+LL9)/2
	if len(row9_fi.get())==0:
		f9 = 0
	else:
		f9 = int(row9_fi.get())
	fix9 = x9*f9
	row9_xi = Label(root, text=x9, width=10, bg="#E7E4E7", justify=CENTER).grid(row=9, column=2)
	row9_fixi = Label(root, text=fix9, width=10, bg="#E7E4E7", justify=CENTER).grid(row=9, column=4)

	x10 = (UL10+LL10)/2
	if len(row10_fi.get())==0:
		f10 = 0
	else:
		f10 = int(row10_fi.get())
	fix10 = x10*f10
	row10_xi = Label(root, text=x10, width=10, bg="#E7E4E7", justify=CENTER).grid(row=10, column=2)
	row10_fixi = Label(root, text=fix10, width=10, bg="#E7E4E7", justify=CENTER).grid(row=10, column=4)

	sum_fixi = fix1+fix2+fix3+fix4+fix5+fix6+fix7+fix8+fix9+fix10
	sum_fi = f1+f2+f3+f4+f5+f6+f7+f8+f9+f10
	if sum_fi == 0:
		sum_fi=1
	else:
		sum_fi = f1+f2+f3+f4+f5+f6+f7+f8+f9+f10
	mean = sum_fixi/sum_fi # Converting mean to string to decrease size and then back to float
	mean = str(mean)
	mean = mean[0:7]
	mean=float(mean)
	mean_A = Label(root, text=mean, bg="#E7E4E7", width=11).grid(row=14, column=1)
	mean_dv_A = Label(root, text="N.A.", bg="#E7E4E7", width=11).grid(row=15, column=1)

	# FOR MEAN DEVIATION ABOUT MEAN
	mean_x1 = str(abs(mean-x1))
	mean_x1 = float(mean_x1[0:7])
	fi_mean_x1 = str(mean_x1*f1)
	fi_mean_x1 = float(fi_mean_x1[0:7])
	row1_mean_x1 = Label(root, text=mean_x1, bg="#E7E4E7", width=10).grid(row=1, column=5)
	row1_fi_mean_x1 = Label(root, text=fi_mean_x1, bg="#E7E4E7", width=10).grid(row=1, column=6)

	mean_x2 = str(abs(mean-x2))
	mean_x2 = float(mean_x2[0:7])
	fi_mean_x2 = str(mean_x2*f2)
	fi_mean_x2 = float(fi_mean_x2[0:7])
	row2_mean_x2 = Label(root, text=mean_x2, bg="#E7E4E7", width=10).grid(row=2, column=5)
	row2_fi_mean_x2 = Label(root, text=fi_mean_x2, bg="#E7E4E7", width=10).grid(row=2, column=6)

	mean_x3 = str(abs(mean-x3))
	mean_x3 = float(mean_x3[0:7])
	fi_mean_x3 = str(mean_x3*f3)
	fi_mean_x3 = float(fi_mean_x3[0:7])
	row3_mean_x3 = Label(root, text=mean_x3, bg="#E7E4E7", width=10).grid(row=3, column=5)
	row3_fi_mean_x3 = Label(root, text=fi_mean_x3, bg="#E7E4E7", width=10).grid(row=3, column=6)

	mean_x4 = str(abs(mean-x4))
	mean_x4 = float(mean_x4[0:7])
	fi_mean_x4 = str(mean_x4*f4)
	fi_mean_x4 = float(fi_mean_x4[0:7])
	row4_mean_x4 = Label(root, text=mean_x4, bg="#E7E4E7", width=10).grid(row=4, column=5)
	row4_fi_mean_x4 = Label(root, text=fi_mean_x4, bg="#E7E4E7", width=10).grid(row=4, column=6)

	mean_x5 = str(abs(mean-x5))
	mean_x5 = float(mean_x5[0:7])
	fi_mean_x5 = str(mean_x5*f5)
	fi_mean_x5 = float(fi_mean_x5[0:7])
	row5_mean_x5 = Label(root, text=mean_x5, bg="#E7E4E7", width=10).grid(row=5, column=5)
	row5_fi_mean_x5 = Label(root, text=fi_mean_x5, bg="#E7E4E7", width=10).grid(row=5, column=6)

	mean_x6 = str(abs(mean-x6))
	mean_x6 = float(mean_x6[0:7])
	fi_mean_x6 = str(mean_x6*f6)
	fi_mean_x6 = float(fi_mean_x6[0:7])
	row6_mean_x6 = Label(root, text=mean_x6, bg="#E7E4E7", width=10).grid(row=6, column=5)
	row6_fi_mean_x6 = Label(root, text=fi_mean_x6, bg="#E7E4E7", width=10).grid(row=6, column=6)

	mean_x7 = str(abs(mean-x7))
	mean_x7 = float(mean_x7[0:7])
	fi_mean_x7 = str(mean_x7*f7)
	fi_mean_x7 = float(fi_mean_x7[0:7])
	row7_mean_x7 = Label(root, text=mean_x7, bg="#E7E4E7", width=10).grid(row=7, column=5)
	row7_fi_mean_x7 = Label(root, text=fi_mean_x7, bg="#E7E4E7", width=10).grid(row=7, column=6)

	mean_x8 = str(abs(mean-x8))
	mean_x8 = float(mean_x8[0:7])
	fi_mean_x8 = str(mean_x8*f8)
	fi_mean_x8 = float(fi_mean_x8[0:7])
	row8_mean_x8 = Label(root, text=mean_x8, bg="#E7E4E7", width=10).grid(row=8, column=5)
	row8_fi_mean_x8 = Label(root, text=fi_mean_x8, bg="#E7E4E7", width=10).grid(row=8, column=6)

	mean_x9 = str(abs(mean-x9))
	mean_x9 = float(mean_x9[0:7])
	fi_mean_x9 = str(mean_x9*f9)
	fi_mean_x9 = float(fi_mean_x9[0:7])
	row9_mean_x9 = Label(root, text=mean_x9, bg="#E7E4E7", width=10).grid(row=9, column=5)
	row9_fi_mean_x9 = Label(root, text=fi_mean_x9, bg="#E7E4E7", width=10).grid(row=9, column=6)

	mean_x10 = str(abs(mean-x10))
	mean_x10 = float(mean_x10[0:7])
	fi_mean_x10 = str(mean_x10*f10)
	fi_mean_x10 = float(fi_mean_x10[0:7])
	row10_mean_x10 = Label(root, text=mean_x10, bg="#E7E4E7", width=10).grid(row=10, column=5)
	row10_fi_mean_x10 = Label(root, text=fi_mean_x10, bg="#E7E4E7", width=10).grid(row=10, column=6)

	md_mean = (fi_mean_x1 + fi_mean_x2 + fi_mean_x3 + fi_mean_x4 + fi_mean_x5 + fi_mean_x6 + fi_mean_x7 + fi_mean_x8 + fi_mean_x9 + fi_mean_x10)/sum_fi
	md_mean = str(md_mean)
	md_mean = float(md_mean[0:7])	
	mean_dv_A = Label(root, text=md_mean, bg="#E7E4E7", width=11).grid(row=15, column=1)

	# For cumulative frequency
	cf1 = Label(root, text=f1, bg="#E7E4E7", width=5).grid(row=1, column=7)
	cf2 = Label(root, text=f1+f2, bg="#E7E4E7", width=5).grid(row=2, column=7)
	cf3 = Label(root, text=f1+f2+f3, bg="#E7E4E7", width=5).grid(row=3, column=7)
	cf4 = Label(root, text=f1+f2+f3+f4, bg="#E7E4E7", width=5).grid(row=4, column=7)
	cf5 = Label(root, text=f1+f2+f3+f4+f5, bg="#E7E4E7", width=5).grid(row=5, column=7)
	cf6 = Label(root, text=f1+f2+f3+f4+f5+f6, bg="#E7E4E7", width=5).grid(row=6, column=7)
	cf7 = Label(root, text=f1+f2+f3+f4+f5+f6+f7, bg="#E7E4E7", width=5).grid(row=7, column=7)
	cf8 = Label(root, text=f1+f2+f3+f4+f5+f6+f7+f8, bg="#E7E4E7", width=5).grid(row=8, column=7)
	cf9 = Label(root, text=f1+f2+f3+f4+f5+f6+f7+f8+f9, bg="#E7E4E7", width=5).grid(row=9, column=7)
	cf10 = Label(root, text=f1+f2+f3+f4+f5+f6+f7+f8+f9+f10, bg="#E7E4E7", width=5).grid(row=10, column=7)	

	# Median Logic Running
	ul=[row1_CIb.get(), UL2, UL3, UL4, UL5, UL6, UL7, UL8, UL9, UL10]
	ll=[row1_CIa.get(), LL2, LL3, LL4, LL5, LL6, LL7, LL8, LL9, LL10]
	f=[f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
	cf=[f1, f1+f2, f1+f2+f3, f1+f2+f3+f4, f1+f2+f3+f4+f5, f1+f2+f3+f4+f5+f6, f1+f2+f3+f4+f5+f6+f7, f1+f2+f3+f4+f5+f6+f7+f8, f1+f2+f3+f4+f5+f6+f7+f8+f9, f1+f2+f3+f4+f5+f6+f7+f8+f9+f10]
	# Finding cf and calculating median
	N=(f1+f2+f3+f4+f5+f6+f7+f8+f9+f10)/2
	for i in range(10):
		if N>cf[i]:
			cf[i]=cf[i]
		else:
			cf_final=cf[i-1]
			ll_final=ll[i]
			f_final=f[i]
			break
	h_final=float(row1_CIb.get())-float(row1_CIa.get())
	median=ll_final + (((N-cf_final)/f_final)*h_final)
	median=str(median)
	median=float(median[0:7])
	median_A = Label(root, text=median, width=5, bg="#E7E4E7").grid(row=16, column=1)

	# Calculating mean deviation about median
	median_x1 = str(abs(median-x1))
	median_x1 = float(median_x1[0:7])

	median_x2 = str(abs(median-x2))
	median_x2 = float(median_x2[0:7])

	median_x3 = str(abs(median-x3))
	median_x3 = float(median_x3[0:7])

	median_x4 = str(abs(median-x4))
	median_x4 = float(median_x4[0:7])

	median_x5 = str(abs(median-x5))
	median_x5 = float(median_x5[0:7])

	median_x6 = str(abs(median-x6))
	median_x6 = float(median_x6[0:7])

	median_x7 = str(abs(median-x7))
	median_x7 = float(median_x7[0:7])

	median_x8 = str(abs(median-x8))
	median_x8 = float(median_x8[0:7])

	median_x9 = str(abs(median-x9))
	median_x9 = float(median_x9[0:7])

	median_x10 = str(abs(median-x10))
	median_x10 = float(median_x10[0:7]) 

	# Placing median - x1
	row1_median_x1 = Label(root, text=median_x1, bg="#E7E4E7", width=11).grid(row=1, column=8)
	row2_median_x2 = Label(root, text=median_x2, bg="#E7E4E7", width=11).grid(row=2, column=8)
	row3_median_x3 = Label(root, text=median_x3, bg="#E7E4E7", width=11).grid(row=3, column=8)
	row4_median_x4 = Label(root, text=median_x4, bg="#E7E4E7", width=11).grid(row=4, column=8)
	row5_median_x5 = Label(root, text=median_x5, bg="#E7E4E7", width=11).grid(row=5, column=8)
	row6_median_x6 = Label(root, text=median_x6, bg="#E7E4E7", width=11).grid(row=6, column=8)
	row7_median_x7 = Label(root, text=median_x7, bg="#E7E4E7", width=11).grid(row=7, column=8)
	row8_median_x8 = Label(root, text=median_x8, bg="#E7E4E7", width=11).grid(row=8, column=8)
	row9_median_x9 = Label(root, text=median_x9, bg="#E7E4E7", width=11).grid(row=9, column=8)
	row10_median_x10 = Label(root, text=median_x10, bg="#E7E4E7", width=11).grid(row=10, column=8)	

	# Calculating fi|median-xi|
	f1_median_x1 = str(f1*median_x1)
	f1_median_x1 = float(f1_median_x1[0:7])

	f2_median_x2 = str(f2*median_x2)
	f2_median_x2 = float(f2_median_x2[0:7])

	f3_median_x3 = str(f3*median_x3)
	f3_median_x3 = float(f3_median_x3[0:7])

	f4_median_x4 = str(f4*median_x4)
	f4_median_x4 = float(f4_median_x4[0:7])

	f5_median_x5 = str(f5*median_x5)
	f5_median_x5 = float(f5_median_x5[0:7])

	f6_median_x6 = str(f6*median_x6)
	f6_median_x6 = float(f6_median_x6[0:7])

	f7_median_x7 = str(f7*median_x7)
	f7_median_x7 = float(f7_median_x7[0:7])

	f8_median_x8 = str(f8*median_x8)
	f8_median_x8 = float(f8_median_x8[0:7])

	f9_median_x9 = str(f9*median_x9)
	f9_median_x9 = float(f9_median_x9[0:7])

	f10_median_x10 = str(f10*median_x10)
	f10_median_x10 = float(f10_median_x10[0:7])

	# Placing fi|median-xi|
	row1_f1_median_x1 = Label(root, text=f1_median_x1, bg="#E7E4E7", width=11).grid(row=1, column=9)
	row2_f2_median_x2 = Label(root, text=f2_median_x2, bg="#E7E4E7", width=11).grid(row=2, column=9)
	row3_f3_median_x3 = Label(root, text=f3_median_x3, bg="#E7E4E7", width=11).grid(row=3, column=9)
	row4_f4_median_x4 = Label(root, text=f4_median_x4, bg="#E7E4E7", width=11).grid(row=4, column=9)
	row5_f5_median_x5 = Label(root, text=f5_median_x5, bg="#E7E4E7", width=11).grid(row=5, column=9)
	row6_f6_median_x6 = Label(root, text=f6_median_x6, bg="#E7E4E7", width=11).grid(row=6, column=9)
	row7_f7_median_x7 = Label(root, text=f7_median_x7, bg="#E7E4E7", width=11).grid(row=7, column=9)
	row8_f8_median_x8 = Label(root, text=f8_median_x8, bg="#E7E4E7", width=11).grid(row=8, column=9)
	row9_f9_median_x9 = Label(root, text=f9_median_x9, bg="#E7E4E7", width=11).grid(row=9, column=9)
	row10_f10_median_x10 = Label(root, text=f10_median_x10, bg="#E7E4E7", width=11).grid(row=10, column=9)

	md_median=(f1_median_x1+f2_median_x2+f3_median_x3+f4_median_x4+f5_median_x5+f6_median_x6+f7_median_x7+f8_median_x8+f9_median_x9+f10_median_x10)/sum_fi
	md_median=str(md_median)
	md_median=float(md_median[0:7])
	median_dv_A = Label(root, text=md_median, bg="#E7E4E7").grid(row=17, column=1)

	# (mean-xi)**2
	mean2_x1 = str(mean_x1**2)
	mean2_x1 = float(mean2_x1[0:7])

	mean2_x2 = str(mean_x2**2)
	mean2_x2 = float(mean2_x2[0:7])

	mean2_x3 = str(mean_x3**2)
	mean2_x3 = float(mean2_x3[0:7])

	mean2_x4 = str(mean_x4**2)
	mean2_x4 = float(mean2_x4[0:7])

	mean2_x5 = str(mean_x5**2)
	mean2_x5 = float(mean2_x5[0:7])

	mean2_x6 = str(mean_x6**2)
	mean2_x6 = float(mean2_x6[0:7])

	mean2_x7 = str(mean_x7**2)
	mean2_x7 = float(mean2_x7[0:7])

	mean2_x8 = str(mean_x8**2)
	mean2_x8 = float(mean2_x8[0:7])

	mean2_x9 = str(mean_x9**2)
	mean2_x9 = float(mean2_x9[0:7])

	mean2_x10 = str(mean_x10**2)
	mean2_x10 = float(mean2_x10[0:7])

	row1_mean2x1 = Label(root, text=mean2_x1, bg="#E7E4E7", width=13).grid(row=1, column=10)
	row2_mean2x2 = Label(root, text=mean2_x2, bg="#E7E4E7", width=13).grid(row=2, column=10)
	row3_mean2x3 = Label(root, text=mean2_x3, bg="#E7E4E7", width=13).grid(row=3, column=10)
	row4_mean2x4 = Label(root, text=mean2_x4, bg="#E7E4E7", width=13).grid(row=4, column=10)
	row5_mean2x5 = Label(root, text=mean2_x5, bg="#E7E4E7", width=13).grid(row=5, column=10)
	row6_mean2x6 = Label(root, text=mean2_x6, bg="#E7E4E7", width=13).grid(row=6, column=10)
	row7_mean2x7 = Label(root, text=mean2_x7, bg="#E7E4E7", width=13).grid(row=7, column=10)
	row8_mean2x8 = Label(root, text=mean2_x8, bg="#E7E4E7", width=13).grid(row=8, column=10)
	row9_mean2x9 = Label(root, text=mean2_x9, bg="#E7E4E7", width=13).grid(row=9, column=10)
	row10_mean2x10 = Label(root, text=mean2_x10, bg="#E7E4E7", width=13).grid(row=10, column=10)

	# fi|mean-xi|**2
	fimean2_x1 = str(mean2_x1*f1)
	fimean2_x1 = float(fimean2_x1[0:7])

	fimean2_x2 = str(mean2_x2*f2)
	fimean2_x2 = float(fimean2_x2[0:7])

	fimean2_x3 = str(mean2_x3*f3)
	fimean2_x3 = float(fimean2_x3[0:7])

	fimean2_x4 = str(mean2_x4*f4)
	fimean2_x4 = float(fimean2_x4[0:7])

	fimean2_x5 = str(mean2_x5*f5)
	fimean2_x5 = float(fimean2_x5[0:7])

	fimean2_x6 = str(mean2_x6*f6)
	fimean2_x6 = float(fimean2_x6[0:7])

	fimean2_x7 = str(mean2_x7*f7)
	fimean2_x7 = float(fimean2_x7[0:7])

	fimean2_x8 = str(mean2_x8*f8)
	fimean2_x8 = float(fimean2_x8[0:7])

	fimean2_x9 = str(mean2_x9*f9)
	fimean2_x9 = float(fimean2_x9[0:7])

	fimean2_x10 = str(mean2_x10*f10)
	fimean2_x10 = float(fimean2_x10[0:7])

	row1_fimean2x1 = Label(root, text=fimean2_x1, bg="#E7E4E7", width=15).grid(row=1, column=11)
	row2_fimean2x2 = Label(root, text=fimean2_x2, bg="#E7E4E7", width=15).grid(row=2, column=11)
	row3_fimean2x3 = Label(root, text=fimean2_x3, bg="#E7E4E7", width=15).grid(row=3, column=11)
	row4_fimean2x4 = Label(root, text=fimean2_x4, bg="#E7E4E7", width=15).grid(row=4, column=11)
	row5_fimean2x5 = Label(root, text=fimean2_x5, bg="#E7E4E7", width=15).grid(row=5, column=11)
	row6_fimean2x6 = Label(root, text=fimean2_x6, bg="#E7E4E7", width=15).grid(row=6, column=11)
	row7_fimean2x7 = Label(root, text=fimean2_x7, bg="#E7E4E7", width=15).grid(row=7, column=11)
	row8_fimean2x8 = Label(root, text=fimean2_x8, bg="#E7E4E7", width=15).grid(row=8, column=11)
	row9_fimean2x9 = Label(root, text=fimean2_x9, bg="#E7E4E7", width=15).grid(row=9, column=11)
	row10_fimean2x10 = Label(root, text=fimean2_x10, bg="#E7E4E7", width=15).grid(row=10, column=11)

	# Variance and Standard Deviation and coefficient of variation
	sum_fimean2_xi = fimean2_x1+fimean2_x2+fimean2_x3+fimean2_x4+fimean2_x5+fimean2_x6+fimean2_x7+fimean2_x8+fimean2_x9+fimean2_x10
	variance=str(sum_fimean2_xi/sum_fi)
	variance = float(variance[0:7])
	sd=str(variance**(0.5))
	sd=float(sd[0:7])
	cv=str((sd/mean)*100)
	cv=cv[0:7]
	variance_A = Label(root, text=variance, bg="#E7E4E7").grid(row=18, column=1)
	sd_A =  Label(root, text=sd, bg="#E7E4E7").grid(row=19, column=1)
	cv_A = Label(root, text=cv+"%", bg="#E7E4E7").grid(row=20, column=1)


# Defining Headers
row0_CIa = Label(root, text="Lower Limit", width=16, height=2, bg="#958D95")
row0_CIb = Label(root, text="Upper Limit", width=13, height=2, bg="#958D95")

row0_xi = Label(root, text="xi", width=10, height=2, bg="#958D95")

row0_fi = Label(root, text="fi", width=5, height=2, bg="#958D95")

row0_fixi = Label(root, text="fixi", width=10, height=2, bg="#958D95")
row0_meanxi = Label(root, text="|mean-xi|", width=10, height=2, bg="#958D95")
row0_fimeanxi = Label(root, text="fi|mean-xi|", width=10, height=2, bg="#958D95")

row0_cf = Label(root, text="cf", width=5, height=2, bg="#958D95")
row0_medianxi = Label(root, text="|median-xi|", width=11, height=2, bg="#958D95")
row0_fimedianxi = Label(root, text="fi|median-xi|", width=13, height=2, bg="#958D95")

row0_meanxi2 = Label(root, text="|mean-xi|**2", width=13, height=2, bg="#958D95")
row0_fimeanxi2 = Label(root, text="fi|mean-xi|**2", width=15, height=2, bg="#958D95")

# Placing Headers
row0_CIa.grid(row=0, column=0)
row0_CIb.grid(row=0, column=1)
row0_xi.grid(row=0, column=2)
row0_fi.grid(row=0, column=3)
row0_fixi.grid(row=0, column=4)
row0_meanxi.grid(row=0, column=5)
row0_fimeanxi.grid(row=0, column=6)
row0_cf.grid(row=0, column=7)
row0_medianxi.grid(row=0, column=8)
row0_fimedianxi.grid(row=0, column=9)
row0_meanxi2.grid(row=0, column=10)
row0_fimeanxi2.grid(row=0, column=11)

# Defining Class Interval Lower Limit Inputs 
row1_CIa = Entry(root, bg="#E7E4E7", width=13, justify=CENTER)
row2_CIa = Label(root, bg="#E7E4E7", width=13, text="0")
row3_CIa = Label(root, bg="#E7E4E7", width=13, text="0")
row4_CIa = Label(root, bg="#E7E4E7", width=13, text="0")
row5_CIa = Label(root, bg="#E7E4E7", width=13, text="0")
row6_CIa = Label(root, bg="#E7E4E7", width=13, text="0")
row7_CIa = Label(root, bg="#E7E4E7", width=13, text="0")
row8_CIa = Label(root, bg="#E7E4E7", width=13, text="0")
row9_CIa = Label(root, bg="#E7E4E7", width=13, text="0")
row10_CIa = Label(root, bg="#E7E4E7", width=13, text="0")

# Placing Class Interval Lower Limit Inputs
row1_CIa.grid(row=1, column=0)
row2_CIa.grid(row=2, column=0)
row3_CIa.grid(row=3, column=0)
row4_CIa.grid(row=4, column=0)
row5_CIa.grid(row=5, column=0)
row6_CIa.grid(row=6, column=0)
row7_CIa.grid(row=7, column=0)
row8_CIa.grid(row=8, column=0)
row9_CIa.grid(row=9, column=0)
row10_CIa.grid(row=10, column=0)

# Defining Class Interval Upper Limit Inputs 
row1_CIb = Entry(root, bg="#E7E4E7", width=13, justify=CENTER)
row2_CIb = Label(root, bg="#E7E4E7", width=13, text="0")
row3_CIb = Label(root, bg="#E7E4E7", width=13, text="0")
row4_CIb = Label(root, bg="#E7E4E7", width=13, text="0")
row5_CIb = Label(root, bg="#E7E4E7", width=13, text="0")
row6_CIb = Label(root, bg="#E7E4E7", width=13, text="0")
row7_CIb = Label(root, bg="#E7E4E7", width=13, text="0")
row8_CIb = Label(root, bg="#E7E4E7", width=13, text="0")
row9_CIb = Label(root, bg="#E7E4E7", width=13, text="0")
row10_CIb = Label(root, bg="#E7E4E7", width=13, text="0")

# Placing Class Interval Upper Limit Inputs
row1_CIb.grid(row=1, column=1)
row2_CIb.grid(row=2, column=1)
row3_CIb.grid(row=3, column=1)
row4_CIb.grid(row=4, column=1)
row5_CIb.grid(row=5, column=1)
row6_CIb.grid(row=6, column=1)
row7_CIb.grid(row=7, column=1)
row8_CIb.grid(row=8, column=1)
row9_CIb.grid(row=9, column=1)
row10_CIb.grid(row=10, column=1)

# Defined Frequency
row1_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)
row2_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)
row3_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)
row4_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)
row5_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)
row6_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)
row7_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)
row8_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)
row9_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)
row10_fi = Entry(root, bg="#E7E4E7", width=5, justify=CENTER)

# Placing Frequency
row1_fi.grid(row=1, column=3)
row2_fi.grid(row=2, column=3)
row3_fi.grid(row=3, column=3)
row4_fi.grid(row=4, column=3)
row5_fi.grid(row=5, column=3)
row6_fi.grid(row=6, column=3)
row7_fi.grid(row=7, column=3)
row8_fi.grid(row=8, column=3)
row9_fi.grid(row=9, column=3)
row10_fi.grid(row=10, column=3)

# Defined Class Mark Label
row1_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row2_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row3_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row4_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row5_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row6_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row7_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row8_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row9_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row10_xi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)

# Placing Class Mark Label
row1_xi.grid(row=1, column=2)
row2_xi.grid(row=2, column=2)
row3_xi.grid(row=3, column=2)
row4_xi.grid(row=4, column=2)
row5_xi.grid(row=5, column=2)
row6_xi.grid(row=6, column=2)
row7_xi.grid(row=7, column=2)
row8_xi.grid(row=8, column=2)
row9_xi.grid(row=9, column=2)
row10_xi.grid(row=10, column=2) 

# Defined xifi Label
row1_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row2_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row3_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row4_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row5_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row6_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row7_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row8_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row9_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)
row10_fixi = Label(root, text="", width=10, bg="#E7E4E7", justify=CENTER)

# Placing xifi Label
row1_fixi.grid(row=1, column=4)
row2_fixi.grid(row=2, column=4)
row3_fixi.grid(row=3, column=4)
row4_fixi.grid(row=4, column=4)
row5_fixi.grid(row=5, column=4)
row6_fixi.grid(row=6, column=4)
row7_fixi.grid(row=7, column=4)
row8_fixi.grid(row=8, column=4)
row9_fixi.grid(row=9, column=4)
row10_fixi.grid(row=10, column=4)

# Defining and placing divider 1
col0_divb = Label(root, width=11, height=1, bg="#E7E4E7").grid(row=11, column=0)
col1_divb = Label(root, width=11, height=1, bg="#E7E4E7").grid(row=11, column=1)
col2_divb = Label(root, width=10, height=1, bg="#E7E4E7").grid(row=11, column=2)
col3_divb = Label(root, width=5, height=1, bg="#E7E4E7").grid(row=11, column=3)
col4_divb = Label(root, width=10, height=1, bg="#E7E4E7").grid(row=11, column=4)

col0_divc = Label(root, width=11, height=1, bg="#E7E4E7").grid(row=13, column=0)
col1_divc = Label(root, width=11, height=1, bg="#E7E4E7").grid(row=13, column=1)
col2_divc = Label(root, width=10, height=1, bg="#E7E4E7").grid(row=13, column=2)
col3_divc = Label(root, width=5, height=1, bg="#E7E4E7").grid(row=13, column=3)
col4_divc = Label(root, width=10, height=1, bg="#E7E4E7").grid(row=13, column=4)

# Defining and placing buttons
submit_button = Button(root, text="Compute", bg="#2D2B2D", fg="white", width=8, command=compute)
submit_button.config(font=("Arial Rounded MT Bold", 10))
submit_button.grid(row=12, column=5)

# Defining and placing Answer Markers
mean_Q = Label(root, text="Mean: ", bg="#E7E4E7").grid(row=14, column=0)
mean_dv_Q = Label(root, text="MD(mean): ", bg="#E7E4E7").grid(row=15, column=0)
median_Q = Label(root, text="Median: ", bg="#E7E4E7").grid(row=16, column=0)
median_dv_Q = Label(root, text="MD(median): ", bg="#E7E4E7").grid(row=17, column=0)
variance_Q = Label(root, text="Variance: ", bg="#E7E4E7").grid(row=18, column=0)
sd_Q =  Label(root, text="Standard Deviation: ", bg="#E7E4E7").grid(row=19, column=0)
cv_Q = Label(root, text="C.V: ", bg="#E7E4E7").grid(row=20, column=0)

# Defining and placing divider 2
col0_diva = Label(root, width=11, height=1, bg="#E7E4E7").grid(row=21, column=0)
col1_diva = Label(root, width=11, height=1, bg="#E7E4E7").grid(row=21, column=1)
col2_diva = Label(root, width=10, height=1, bg="#E7E4E7").grid(row=21, column=2)
col3_diva = Label(root, width=5, height=1, bg="#E7E4E7").grid(row=21, column=3)
col4_diva = Label(root, width=10, height=1, bg="#E7E4E7").grid(row=21, column=4)

window.mainloop()
