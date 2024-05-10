import {LightningElement} from 'lwc';
import {loadScript} from "lightning/platformResourceLoader";

export default class Ecomm_stripeTest extends LightningElement {
 
    async loadElements() {
        console.log('Loading Stripe Elements');

        const stripe = Stripe('[Stripe Public Key]');

        const options = {
            mode: 'setup',
            currency: 'usd',
            paymentMethodTypes: ['card']
        };

        const elements = stripe.elements(options);
        
        const paymentElement = elements.create('payment');

        paymentElement.mount(this.refs.paymentElement);

        const form = this.refs.paymentForm;
        const submitBtn = this.refs.submit;
        
        const handleError = (error) => {
            console.log(error);
            const messageContainer = this.refs.errorMessage;
            messageContainer.textContent = error.message;
            submitBtn.disabled = false;
        }

        form.addEventListener('submit', async (event) => {
            console.log('Clicked submit');
            event.preventDefault();

            if (submitBtn.disabled) {
                return;
            }

            submitBtn.disabled = true;

            const {error: submitError} = await elements.submit();
            if (submitError) {
                handleError(submitError);
                return;
            }

            const {error} = await stripe.confirmSetup({
                elements,
                confirmParams: {
                    return_url: window.location.href,
                },
            });
            if (error) {
                handleError(error);
            }
        });
        
    }

    renderedCallback() {
        this.loadStripeScript();
    }

    loadStripeScript() {
        if (this.stripeLoaded) { return; }
        let self = this;
        loadScript(this, 'https://js.stripe.com/v3/').then(() => { 
            self.loadElements();
        });
        this.stripeLoaded = true;
    }

}