#Week 1 Matlab/Octave Quiz
#1
[1;2;3]

[1 2 3]'

#2
A=[1,2,3;2,3,4;3,4,5;4,5,6]
#A(:,2:3)

#3
A=[1,2;3,4]
B=[2,2;3,3;4,4]
C=eye(3)
d=[1,2,3]
E=zeros(3,3)
#A*B'
#C.*E
#d*B
#C*E

#4
B=[2,2;3,3;4,4]
d=[1,2,3]
f=[8;9]
#B + repmat(f',3,1)
#B - [d' d'*2]

#5
#4x1 vector that contains number 5 in every position
#ones(4,1)*5

#6
#[A(:,1) A(:,3) A(:,5)]
#A(:,1:2:5)

#7
y=sin(x.^2);
x=0:0.05:5;
plot(x,y);

#8
A = [1 0 -4 8 3; 4 -2 3 3 1];

b = zeros(1,5);

for index = 1:size(A,2)

if A(1,index) > A(2,index)

b(index) = A(1,index);

else

b(index) = A(2,index);

end

end
#b=[4,0,3,8,3]

#9
x = 1;

while x > 1e-5

x = x / 2;

end
#x=7.63e-06

#10
#zeros(2,3)

#11
#sets all negative entries to 0
#A(A<0)=0

#12
#A=[1;2;3]
#B=[-1;-2;-3]
#C=A.*B

#13
#returns the index of the first element to x equal to 3
#find(x == 3,1)

#14
#keyboard command is for debugging