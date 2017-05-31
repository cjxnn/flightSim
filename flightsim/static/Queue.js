class Queue{
	constructor(){
		this.data = [];
	}
	
	get length(){
		return this.data.length;
	}
	
	get isEmpty(){
		return !this.data.length;
	}
	
	get peek(){
		return this.data[0];
	}
	
	enqueue(element){
		this.data.push(element);
	}
	
	dequeue(){
		return this.data.shift();
	}
}