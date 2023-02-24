// Here is a snipped from an Analysis of the APT Tulra Malware, decompiled and analysed by GhidrAI:

//F_START:  FUN_00401000()
LRESULT handleWindowMsg(HWND windowHandle, UINT msgType, WPARAM wParam, int lParam) 
    {
    int color1;
    int color2;
    LRESULT resultValue;
    HDC deviceContext;
    HBRUSH brushColor;  // Color of the brush used in drawing.  				     // It is set by CreateBrushIndirect function.     		     
                                                                            // The parameters are taken from globalVar0042eb70 array.  

    HFONT fontObject;                                                         // Handle to a font object created by CreateFontIndirectA().  
    HGDIOBJ hGdiObj;                                                         // Temporary handle to an object returned after SelectObject().
    int localVar4 ;       
    tagPAINTSTRUCT paintStructVarible ;                    
     tagRECT rectVariable ;        // To store the client rectangle values got from GetClientRect() API call.                     
     LOGBRUSH logBrushVariable ;               // Structure that contains information about a logical brush that can be used for painting operations.                  iVar1 = globalVar0042eb70[];                /*Initializing variable with value stored at Global Variable*/              if (msgType == 0xf) {                       /*If Message type is equal to 0x0f */           deviceContext = BeginPaint(windowHandle , &paintStructVarible);            logBrushVariable . lbStyle=0 ;                        /*Setting style of Logical Brush*/             GetClientRect(windowHandle , &rectVariable );                    /*Getting Client Rectangle Co-ordinates and storing them in rectVariables */            color2 = rectVariable . bottom ;         /*Storing Bottom co-ordinate in another variable as it will be used repeatedly.*/          rectVariable . bottom=0 ;               /* Setting Bottom co-ordinate of Rectangle to 0*/            for (/*No initialization required as all variables are already initialized before loop starts */  ;; ) {                   local var4 =color2 -rectVariabel . top  ;              /*Subtracting Top Co-ordinate from Bottom Co-ordinate and storing resultant in Local variable 4*/                logBrushvariable . lbColor=(uint)(CONCAT11((char)((int)(globalvar0042eb70[8]*localVAr4 + globalvar004ebeb7[9]*rectvariable.top)/color2 ), (char) ((int)(globalvar004ebeb7[7] *localVAr4 +globalvar004ebeb7[10] *rectvariable . top )/color2))<< 8 | (int)((uint)*(byte *)(iVar1 + 0x50)*i


//F_START:
void modify_function(int param1) { 
	uint uVar1;
    uint uVar2;
    uint *puVar3; //a pointer to a unsigned integer type variable. 
    uint uVar4;   //variable of an unsigned integer type. 
    int iVar5;    //integer type variable. 
	int iVar6;  

	//initialize the value of 'uvar1' with the product of 'param1' and 0x418, add 8 and then globalvar0042eb88 will be added to it after casting it
 // into a pointer as a result we get address in memory where some data is stored which is then assigned to 'uvar1'. 
	uVar1 = *(uint *)(param1 * 0x418 + 8 + globalVar0042eb88);
	//check if bitwise AND operation between 2 & uvar 1 returns any non zero value or not if yes execute this block else skip this block.    
	if ((uVar1 & 2) != 0) {
        //assign parameter plus one to uvar4 for further processing within looping condition below.  
        uVarl4 = paraml + 1 ;
        //check if given expression return true or false, if true enter loop else exit from function by returning nothing (void).  
        // In case its true assign product of 'uvarl4' and 0x418, add 8 and then global var 0042eb8c will be added after casting it into a pointer as result we get address in memory where some data is stored which is assigned to pu var 3 (pointer).     
		if (uVarl4 < globalVarl0042eb8c) {         
            puVarl3 = (uint*)(uVarl4*0x418+8+globalVarl0042eb88);                       
            iVarl5 = O ;                           /* assigning Zero */                      do{                             /* start do while loop*/                       /* assign content at location pointed out by pu var 3 */                  /***/                    uvars2=*pu Var3 ;                     /* check following conditions*/                   /* check bitwise AND operation between 2 & U vars 2 returns any non zero value or not.*/                         If((uvars2&2)==O){                          /***/               If((UVARS2& 4)==O){                              /***/                IVAR6=i VAR 5 ;                        /**/*///check bitwise AND operation between 16 & UVars 2 return any non zero value or not .If Yes perform XOR Operation on Uvars l with UVArs 2 ,Perform BitWise AND Operation Between 1 And Result Of Above XOR Operation Finally Assign It Back To Location Pointed By Pu Var 3 Else Do Nothing .       If((U VAR S2&Ox10)= ==O)*PU VA R3=(UVARS l^UVA RSZ )&l ^UVA RS Z**/**/*/+-else-+--IVAR 6=I VaR 5 -+--+--+-IF IvaR 5 ==o RETURN ELSE DO NOTHING.-++---+++ }Else{ IVar 6=iVa r 5 + -I IF i Va r 5 == o RETURN ELSE DO NOTHING.}El se{ IVar 6=iVa r s ++} U va r 4+= l PU VA R 3 += Ox 106 I VaR s =I vaR 6 WHILE(UVaRL<GLOBAL V AR 00 42 EB SC )}RETURN};//F_END


//F_START: 
uint findNextUnusedIndex(uint currIndex,int flag){
	uint *dataPtr;
	int iVar2;
	uint uVar3;
	uint uVar4;
	int iVar5;
	int localVarCnt1; // number of 0 bits in the local scope 
    int localVarCnt2; // number of 1 bits in the local scope
    iVar2 = globalVariableA ; // gets a value from global variable A 
   iVar5 = currIndex * 0x418 + globalVariableA ; // calculates an offset for current index and adds it to globalVariable A
    localVaRCnt1 = 0 ; // set both counters to zero initially. 
    localVaRCnt2 = 0 ; 

     if (((*(uint *)(iVAr5 + 8) & 2) != 0) && (flag !=0 )){ // check if bitmask is not equal to 
       // zero and flag is not equal too. If true increment current index by one and clear bitmask accordingly. ``
